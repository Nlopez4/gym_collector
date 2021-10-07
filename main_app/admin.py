from django.contrib import admin
from .models import gyms, location, times
# Register your models here.
admin.site.register(gyms)
admin.site.register(location)
admin.site.register(times)
