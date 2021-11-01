from django.db import models


class UrlRedirect(models.Model):
    destiny = models.URLField(max_length=512)
    slug = models.SlugField(max_length=128, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class UrlLog(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    origin = models.URLField(max_length=512, null=True, blank=True)
    user_agent = models.CharField(max_length=512, null=True, blank=True)
    host = models.CharField(max_length=512, null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    url_redirect = models.ForeignKey(UrlRedirect, on_delete=models.DO_NOTHING,
                                     related_name='logs')  # logs create automaticly a atribute in UrlRedirect
