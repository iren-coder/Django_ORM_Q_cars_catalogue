from django.contrib import admin

# Register your models here.

from django.contrib import admin

from app.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass