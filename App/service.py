from django.http import HttpResponse
from django.shortcuts import render


def doGetThing(r):
    context = {'hello': 'Hello World!'}
    return render(r, "context")


def doPostThing():
    return HttpResponse('this is a POST request')
