from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Province)
admin.site.register(models.City)
admin.site.register(models.Merchantclass)
admin.site.register(models.Merchant)
admin.site.register(models.User)


