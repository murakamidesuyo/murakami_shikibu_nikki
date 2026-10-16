from django.shortcuts import render
from django.http import HttpResponse   #20060525 shogo add

# Create your views here.
#20060525 shogo add↓
def index(request):
    return HttpResponse('<h1>村上式部日記へようこそ！</h1>')
#20060525 shogo add↑
