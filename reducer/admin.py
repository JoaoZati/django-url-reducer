from django.contrib import admin
from reducer.models import UrlRedirect


@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ('destiny', 'slug', 'create_date', 'update_date',)

    def __str__(self):
        return f'UrlRedirect para {self.slug}'
