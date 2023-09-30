from django.db import models

# Create your models here.

class SecretKeys(models.Model):
    name = models.CharField(max_length=128)
    key = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
