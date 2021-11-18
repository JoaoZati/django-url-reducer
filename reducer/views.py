from django.shortcuts import render, redirect
from reducer.models import UrlRedirect
from reducer.models import UrlLog
from django.db.models.functions import TruncDate
from django.db.models import Count
import requests
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


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
    redirects_date = list(
        UrlRedirect.objects.filter(
            slug=slug
        ).annotate(
            date=TruncDate('logs__create_date')
        ).annotate(
            clicks=Count('date')
        ).order_by('date')
    )
    context = {
        'reduce': url_redirect,
        'url_reduced': url_reduced,
        'redirects_date': redirects_date,
        'total_clicks': sum(r.clicks for r in redirects_date)
    }

    return render(request, 'reduce.html', context)


def home(request):
    if request.method == 'POST':
        url = request.POST['url']
        slug = request.POST['slug']

        try:
            requests.get(url)
        except Exception as e:
            messages.error(request, "Url didn't return a redirect response")
            return render(request, 'index.html')

        try:
            UrlRedirect.objects.get(slug=slug)
        except UrlRedirect.DoesNotExist:
            UrlRedirect.objects.create(
                destiny=url,
                slug=slug,
            )
        return HttpResponseRedirect(reverse('reports', kwargs={'slug': slug}))

    return render(request, 'index.html')
