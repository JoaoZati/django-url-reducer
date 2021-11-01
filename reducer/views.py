from django.shortcuts import render, redirect

from reducer.models import UrlRedirect
from reducer.models import UrlLog


def redirect_url(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    UrlLog.objects.create(
        origin=request.META.get('TTP_REFERER'),
        user_agent=request.META.get('HTTP_USER_AGENT'),
        host=request.META.get('HTTP_HOST'),
        ip=request.META.get('REMOTE_ADDR'),
        url_redirect=url_redirect,
    )

    return redirect(url_redirect.destiny)


def reports(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    url_reduced = request.build_absolute_uri(f'/{slug}')
    context = {
        'reduce': url_redirect,
        'url_reduced': url_reduced,
    }

    return render(request, 'reduce.html', context)
