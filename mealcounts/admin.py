from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Tarikh)
admin.site.register(Member)
admin.site.register(Meal)
admin.site.register(Khoroch)
# admin.site.register(Sheet)


