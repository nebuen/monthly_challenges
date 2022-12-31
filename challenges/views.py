from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    text = None
    if month == 'jan':
        text = "month of january"
    elif month == 'feb':
        text = "month of february"
    else:
        return HttpResponseNotFound("This is not supported")
    return HttpResponse(text)
    