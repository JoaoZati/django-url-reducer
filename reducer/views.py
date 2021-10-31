from django.shortcuts import render, redirect

from reducer.models import UrlRedirect


def redirect_url(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)

    return redirect(url_redirect.destiny)


def reports(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    url_reduced = request.build_absolute_uri(f'/{slug}')
    context = {
        'reduce': url_redirect,
        'url_reduced': url_reduced,
    }

    return render(request, 'reduce.html', context)
