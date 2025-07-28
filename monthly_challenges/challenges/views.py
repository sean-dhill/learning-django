from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

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


def index(request):
    months = list(monthly_challenges_dict.keys())

    return render(request, "challenges/index.html",{
        "months": months
    })

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        return render(request,"challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        raise Http404()


def monthly_challenges_by_num(request, month):
    months = list(monthly_challenges_dict.keys())

    if month > len(months) or month == 0:
        return HttpResponseNotFound("Invalid month")

    redirected_month = months[month - 1]
    # Returns for example /challenges/january if month is 1
    redirected_url = reverse("month-challenge", args=[redirected_month])
    return HttpResponseRedirect(redirected_url)
