from django.shortcuts import render, redirect

def forum_chairman_view(request):
    return render(request, 'coordination_forum/chairman.html', context={'active': 'forum_chairman'})


def forum_members_view(request):
    return render(request, 'coordination_forum/members.html', context={'active': 'forum_members'})


def forum_secretary_view(request):
    return render(request, 'coordination_forum/secretary.html', context={'active': 'forum_secretary'})


def forum_meeting_minutes_view(request):
    return render(request, 'coordination_forum/meeting_minutes.html', context={'active': 'forum_meeting_minutes'})

