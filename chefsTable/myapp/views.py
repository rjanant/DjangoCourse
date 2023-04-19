from django.shortcuts import render
from datetime import  datetime
# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('Welcome to Lemon Tree Restaurant!')

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = """<h1 style = "color: #F4CE14;"> This is Lemon Tree Restaurant</h1>"""
    return HttpResponse(text)

def drinks(request,drink_name):
    drink = {
        'mocha' : 'type of coffee',
        'tea' : 'type of beverage',
        'lemonade' : 'type of refreshment'
    }
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h2> {drink_name} <h2>" + choice_of_drink)

