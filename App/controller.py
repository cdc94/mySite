from django.shortcuts import render

from django.http import HttpRequest
from . import service


def flowStatController(request):
    return service.doGetThing(request)
    # if request.method == 'GET':
    #     service.doGetThing()
    # elif request.method == 'POST':
    #     service.doPostThing()

