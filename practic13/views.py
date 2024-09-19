from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from .models import Profile


@login_required(login_url='login')
def profile_view(req:HttpRequest):
    user = Profile.objects.select_related('user').get(user=req.user)
    return render(req, 'pr13_profile.html', context={
        'user':user
    })
