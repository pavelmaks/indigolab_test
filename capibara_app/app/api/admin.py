from django.contrib import admin
from rest_framework.authtoken.models import Token

from .models import Capibara


@admin.register(Capibara)
class CapibaraAdmin(admin.ModelAdmin):
    pass


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    pass
