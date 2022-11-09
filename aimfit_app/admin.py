from django.contrib import admin

from aimfit_app import models

admin.site.register(models.Login)
admin.site.register(models.Trainer)
admin.site.register(models.Physician)

# Register your models here.
