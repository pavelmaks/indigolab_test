from django.contrib import admin

from .models import Capibara


@admin.register(Capibara)
class AuthorAdmin(admin.ModelAdmin):
    pass
