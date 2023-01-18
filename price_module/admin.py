from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(PriceModule)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "distance_in_meters", "price","tmf_under_hour","tmf_for_two_hour","tmf_for_three_hour")