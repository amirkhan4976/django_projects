from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def printnum(request, guess):
    response = """<html><body>
    <p>Your input number was: """+escape(guess)+"""</p>
    </body></html>"""
    return HttpResponse(response)
