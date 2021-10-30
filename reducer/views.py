from django.shortcuts import render, redirect


# Create your views here.
def redirect_url(request, slug):
    return redirect('https://google.com')
