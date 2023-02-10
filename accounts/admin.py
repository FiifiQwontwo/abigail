from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import EKKPastor, Busscell
from django.contrib import admin

BaseUser = get_user_model()


class EKKPastorAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')


class BusscellAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')


admin.site.register(EKKPastor, EKKPastorAdmin)
admin.site.register(Busscell, BusscellAdmin)
