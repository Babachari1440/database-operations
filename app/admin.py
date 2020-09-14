from django.contrib import admin

# Register your models here.

from app.models import *

#syntax for registering your models
#admin.site.register(modelname)

admin.site.register(Category)
admin.site.register(Myntra)
admin.site.register(Flipcart)
admin.site.register(Customer)