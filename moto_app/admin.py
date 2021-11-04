# from django.contrib import admin

# Register your models here.

# from django.db import models

# Create your models here.
# from django.contrib.auth.models import User
# from django.db import models



from django.contrib import admin
from .models import Owner, Motorycycle, Part, SoldPart


class OwnerAdmin(admin.ModelAdmin):
	list_max_show_all = 1000
	list_per_page = 1000
	list_display = ('name', 'position', 'personal_info', 'email')

admin.site.register(Owner, OwnerAdmin)

class MotorycycleAdmin(admin.ModelAdmin):
	list_max_show_all = 1000
	list_per_page = 1000
	list_display = ('owner', 'motorcycle_brand', 'motorcycle_model', 'vin', 'manufactured_year', 'real_km', 'next_maintenance')

admin.site.register(Motorycycle, MotorycycleAdmin)
admin.site.register(Part)
admin.site.register(SoldPart)
# class PartAdmin(part.PartAdmin):
# 	list_max_show_all = 1000
# 	list_per_page = 1000
# 	list_display = ('name', 'u_m', 'price')
#
# admin.site.register(Part, PartAdmin)


# class PartAdmin(part.PartAdmin):
# 	list_max_show_all = 1000
# 	list_per_page = 1000
# 	list_display = ('name', 'u_m', 'price')
#
# admin.site.register(Part, PartAdmin)








# from django.contrib import admin
#
#
# from moto_app.models import *


# # class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
# class ProductAdmin(ImportExportModelAdmin):
#     # resource_class = Product
#     list_display = ('name', 'description', 'stock', 'price', 'category', 'image', 'promoted')
#     pass

# admin.site.register(Motorycycle)
# admin.site.register(Owner)
# admin.site.register(Service)
# admin.site.register(Part)
# admin.site.register(SoldPart)

