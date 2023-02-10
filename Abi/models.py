from django.db import models


# Create your models here.

class MemberType(models.Model):
    member_type = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
