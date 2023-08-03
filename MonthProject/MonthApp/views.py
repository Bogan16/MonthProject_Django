from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

months = [
    {
        "id": 1,
        "month": "january",
        "plans": "My plans in January",
    },
    {
        "id": 2,
        "month": "february",
        "plans": "My plans in February",
    },
    {
        "id": 3,
        "month": "march",
        "plans": "My plans in March",
    },
    {
        "id": 4,
        "month": "april",
        "plans": "My plans in April",
    },
    {
        "id": 5,
        "month": "may",
        "plans": "My plans in May",
    },
    {
        "id": 6,
        "month": "june",
        "plans": "My plans in June",
    },
    {
        "id": 7,
        "month": "july",
        "plans": "My plans in July",
    },
    {
        "id": 8,
        "month": "august",
        "plans": "My plans in August",
    },
    {
        "id": 9,
        "month": "september",
        "plans": "My plans in September",
    },
    {
        "id": 10,
        "month": "october",
        "plans": "My plans in October",
    },
    {
        "id": 11,
        "month": "november",
        "plans": "My plans in November",
    },
    {
        "id": 12,
        "month": "december",
        "plans": "My plans in December",
    },
]

def redirect_to(request, month_id):
    month = next((m for m in months if m["id"] == month_id), None)
    if month:
        return HttpResponseRedirect(reverse("month_view", args=[month["month"]]))
    else:
        return HttpResponseRedirect(reverse("not_found"))

def month_view(request, month_name):
    month = next((m for m in months if m["month"] == month_name), None)
    if month:
        return HttpResponse(f"Month: {month['month']}, Plans: {month['plans']}")
    else:
        return render(request, "MonthApp/not_found.html")

def home_view(request):
    return render(request, "MonthApp/home.html")

def not_found(request):
    return render(request, "MonthApp/not_found.html")
