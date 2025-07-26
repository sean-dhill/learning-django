from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("Set 3 personal intentions for the year.")

def febuary(request):
    return HttpResponse("Reach out to someone you haven't spoken to in a while.")

def march(request):
    return HttpResponse("Go outside for a 20-minute walk at least 3 times a per week")

def april(request):
    return HttpResponse("Declutter one space in your home")
