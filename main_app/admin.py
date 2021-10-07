from django.contrib import admin
from .models import gyms, location, Class
# Register your models here.
admin.site.register(gyms)
admin.site.register(location)
admin.site.register(Class)
