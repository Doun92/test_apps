from django.contrib import admin

# Register your models here.
from .models import TOTPCode

class TOTPAdmin(admin.ModelAdmin):
    model = TOTPCode
    
    list_display = ["federation", "role"]

admin.site.register(TOTPCode, TOTPAdmin)