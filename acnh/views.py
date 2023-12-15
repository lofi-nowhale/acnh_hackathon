from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    return HttpResponse("Hello,world. You're at the ACNH index!")

def get_villagers(request):
    response = requests.get('')