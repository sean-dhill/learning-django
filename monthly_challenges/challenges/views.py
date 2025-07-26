from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges_dict = {
    "january": "Start a journal and write one sentence per day.",
    "february": "Drink at least 2 liters of water every day.",
    "march": "Walk 10,000 steps each day.",
    "april": "Declutter one space in your home.",
    "may": "Try a new healthy recipe each week.",
    "june": "Wake up 30 minutes earlier and stretch.",
    "july": "Read 10 pages of a book every day.",
    "august": "Limit screen time before bed.",
    "september": "Learn something new each week.",
    "october": "Write down 3 things you're grateful for daily.",
    "november": "Spend 10 minutes meditating every morning.",
    "december": "Do one kind thing for someone each day."
}

# Create your views here.


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Month not supported")

def monthly_challenges_by_num(request, month):
    months = list(monthly_challenges_dict.keys())

    if month > len(months) or month == 0:
        return HttpResponseNotFound("Invalid month")
    
    redirected_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirected_month)