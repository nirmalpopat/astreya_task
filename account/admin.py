from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'wins', 'loses', 'ties')

admin.site.register(Profile, ProfileAdmin)
