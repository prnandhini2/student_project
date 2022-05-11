from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    name="Nandhini"
    return render(request,"index.html",{'name':name})

def about(request):
    return render(request,"about.html")

def welcome(request):
    name="Edubridge Learner"
    return render(request,"welcome.html",{'name':name})

# Create your views here.
