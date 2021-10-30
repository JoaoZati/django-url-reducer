from django.shortcuts import render, redirect


def redirect_url(request, slug):
    return redirect('https://google.com')
