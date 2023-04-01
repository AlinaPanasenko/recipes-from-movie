from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from users.models import Profile


@login_required
def profile(request):
    return render(request, 'profile.html')