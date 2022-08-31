import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    print("here")
    return render(request, 'articles/index.html')

def greeting(request):
    foods = ['apple','orange','banana']
    info = {'name':'Kijun'}

    context ={
        'foods': foods,
        'info': info
    }
    return render(request, 'articles/greeting.html', context)

def dinner(request):
    foods = ['sushi','chicken','hamburger']
    pick =random.choice(foods)
    context = {
        'foods': foods,
        'pick' : pick
    }
    return render(request, 'articles/dinner.html', context)

def throw(request):
    return render(request, "articles/throw.html")

def catch(request):
    data = request.GET.get('message') #input id
    context = {'data':data}
    return render(request, "articles/catch.html",context)

def fake_google(request):
    return render(request, 'articles/fake_google.html')

def hello(request, name):
    context = {'name':name}
    return render(request, 'articles/hello.html', context)