from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page_view(request):
    return HttpResponse('Hello World')


def about_tool(request):
    return HttpResponse('How are you doing')


def rat_tool(request):
    return HttpResponse('have a nice day')


def dense_tool(request):
    return HttpResponse('Sleeps a lot')


def detect_tool(request):
    return HttpResponse('Hunt the prayers')