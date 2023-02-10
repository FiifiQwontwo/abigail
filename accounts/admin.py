from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import EKKPastor, Busscell
from django.contrib import admin

BaseUser = get_user_model()




admin.site.register(EKKPastor)
admin.site.register(Busscell)
admin.site.register(BaseUser)
