from django.contrib import admin

from .models import Property, homeImages, Reserve
# Register your models here.


admin.site.register(Property)
admin.site.register(homeImages)
admin.site.register(Reserve)
