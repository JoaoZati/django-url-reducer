from django.shortcuts import render, redirect

from reducer.models import UrlRedirect


def redirect_url(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    return redirect(url_redirect.destiny)


def reports(request, slug):
    return render(request, 'reduce.html')
