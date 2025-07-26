from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenges(request, month):
    monthly_challenge = None
    if month == "january":
        monthly_challenge = "Set 3 personal intentions for the year."
    elif month == "febuary":
        monthly_challenge = "Reach out to someone you haven't spoken to in a while."
    elif month == "march":
        monthly_challenge = "Go outside for a 20-minute walk at least 3 times a per week"
    elif month == "april":
        monthly_challenge = "Declutter one space in your home"
    else:
        return HttpResponseNotFound("No goal for this month")
    return HttpResponse(monthly_challenge)

def monthly_challenges_by_num(request, month):
    return HttpResponse(month)