from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# 'request' name is convention. It can be some other name too.
def index(request) :    
  return HttpResponse("Hello World")
