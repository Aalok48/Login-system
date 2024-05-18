from django.shortcuts import render, redirect
from django.contrib.auth import logout
from allauth.socialaccount.models import SocialApp
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


def home(request):
    try:
        google_provider = SocialApp.objects.get(provider='google')
    except ObjectDoesNotExist:
        print("No 'google' provider found.")
        raise

    return render(request, 'home.html', {'google_provider': google_provider})


def logout_view(request):
    logout(request)
    return redirect('/')
