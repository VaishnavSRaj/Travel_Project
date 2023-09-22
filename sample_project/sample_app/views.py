from django.http import HttpResponse
from django.shortcuts import render
from .models import place, team


# Create your views here.

def demo(request):
    obj= place.objects.all()
    data = team.objects.all()
    return render(request,'index.html' , {'obj': obj , 'team': data})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     result=x+y
#     return render(request , 'result.html' , {'data': result})