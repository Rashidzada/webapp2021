from django.contrib import admin
from .models import About
# Register your models here.
class AdminAbout(admin.ModelAdmin):
    list_display = ('name','email','address','contact')
admin.site.register(About,AdminAbout)