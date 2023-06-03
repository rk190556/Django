from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.


def index(request):
    my_dict = {"insert_me": "Now I am coming from index.html!"}
    return render(request, "index.html", context=my_dict)
