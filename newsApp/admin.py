from django.contrib import admin
from newsApp import models
# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.Post)
admin.site.register(models.Comment)