from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from registration.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode as b64_encode, urlsafe_base64_decode as b64_decode
from mailgun.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.http import HttpResponse


class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        try:
            email, password = request.POST['email'], request.POST['password']
        except KeyError as e:
            return render(request, 'registration/login.html', context={'error': f'Missing field: {e}'})
        user = authenticate(request, username=email, password=password)

        if user is None:
            error = 'Unable to login, please verify username and password.'
            return render(request, 'registration/login.html', context={'error': error})

        try:
            auth_login(request, user=user)
        except:
            error = 'Unable to login. Please try again in some time.'
            return render(request, 'registration/login.html', context={'error': error})
        if request.POST.get('next', None) is not None:
            return redirect(to=request.POST['next'])
        return redirect(to='home_page')


class LogoutView(View):
    def get(self, request):
        auth_logout(request)
        return redirect(to='home_page')


class PasswordChangeView(LoginRequiredMixin, View):
    login_url = '/login'
    redirect_field_name = 'next'

    def get(self, request):
        return render(request, 'registration/change_password.html')

    def post(self, request):
        try:
            old_pass, new_pass, conf_new_pass = request.POST[
                                                    'old'], request.POST['password1'], request.POST['password2']
        except KeyError as e:
            return render(request, 'registration/change_password.html', context={'error': f'Missing field: {e}.'})
        if request.user.check_password(old_pass):
            if new_pass == conf_new_pass:
                request.user.set_password(new_pass)
                return redirect(to="password_change_done")
            else:
                error = "New passwords do not match."
                return render(request, 'registration/change_password.html', context={'error': error})
        else:
            error = "Old password is wrong."
            return render(request, 'registration/change_password.html', context={'error': error})


class PasswordChangeDoneView(LoginRequiredMixin, View):
    login_url = '/login'
    redirect_field_name = 'next'

    def get(self, request):
        context = {"title": "Password Updated", "heading": "Change Password",
                   "message": "Password Change Successful",
                   "redirect": {"url": 'home_page', "text": 'Go back to home.'}}
        return render(request, 'registration/message.html',
                      context=context)


class PasswordResetView(View):
    def get(self, request):
        return render(request, 'registration/forgot_password.html')


class PasswordResetDoneView(View):
    def post(self, request):
        dtg = default_token_generator
        try:
            email = request.POST['email']
            user = User.objects.get(email=email)
        except KeyError as e:
            error = 'Enter email id.'
            return render(request, 'registration/forgot_password.html', context={'error': error})
        except User.DoesNotExist:
            error = 'No account found with that Email-id.'
            return render(request, 'registration/forgot_password.html', context={'error': error})

        token = dtg.make_token(user)
        uidb64 = b64_encode(bytes(str(user.pk).encode()))
        context = {
            'email': user.email,
            'protocol': 'http',
            'domain': settings.DOMAIN,
            'uid': uidb64,
            'token': token,
            'name': user.first_name,
        }
        mail_body = render_to_string(
            'registration/password_reset_email.html', context=context)
        send_mail("Password Reset", mail_body,
                  [user.email], 'donotreply@example.com')
        message = {"title": "Password Reset", "heading": "Email Sent",
                   "message": "A mail has been sent to your registered email"
                              " with instructions for resetting your password."}
        return render(request, 'registration/message.html', context=message)


class PasswordResetConfirmView(View):
    def get(self, request, uidb64, token):
        print(token)
        dtg = default_token_generator
        try:
            user = User.objects.get(pk=b64_decode(uidb64).decode())
        except:
            return HttpResponse(status=400, content='Bad URL.')
        if dtg.check_token(user, token):
            return render(request, 'registration/reset_password.html', context={'uid': uidb64, 'token': token})
        return HttpResponse(status=400, content='Bad URL.')


class PasswordResetCompleteView(View):
    def post(self, request):
        try:
            uidb64 = request.POST['uid']
            token = request.POST['token']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            user = User.objects.get(pk=b64_decode(uidb64).decode())
            if password1 != password2:
                raise ValueError
            dtg = default_token_generator
            if not dtg.check_token(user, token):
                raise AssertionError
        except KeyError:
            return HttpResponse(status=400, content="Bad Request. Please verify passwords or try again")
        except ValueError:
            return HttpResponse(status=400, content="Bad Request. Passwords do not match.")
        except User.DoesNotExist:
            return HttpResponse(status=400, content="Bad Request.")
        except:
            return HttpResponse(status=400, content="Bad Request.")

        user.set_password(password1)
        user.save()
        message = {"title": "Password Reset", "heading": "Password Changed Successfully",
                   "message": "Your password has been successfully changed. Please Login with your new password.",
                   "redirect": {"url": "login", "text": "Return to Login Page."}}
        return render(request, 'registration/message.html', context=message)
