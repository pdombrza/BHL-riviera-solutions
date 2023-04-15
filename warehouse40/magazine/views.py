from django.shortcuts import render
from django.http import HttpResponse
from .load_example_data import load_example_data


def index(request):
    return HttpResponse("jo")

def load_data(request):
    load_example_data()
    return HttpResponse("")
# Create your views here.
