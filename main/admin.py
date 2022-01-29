from django.contrib import admin
from main.models import ContactUs
# Register your models here.
class ConractUsadmin(admin.ModelAdmin):
    list_display = ("id","name","email", "adress","message","sent_at")

admin.site.register(ContactUs, ConractUsadmin)
