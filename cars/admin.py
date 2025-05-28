from django.contrib import admin
from cars.models import Car, Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model','brand','factory_year','model_year','value')
    search_fields = ('model','brand')

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)


admin.site.site_header = "Frota Origem - Painel Administrativo"
admin.site.site_title = "Painel Administrativo"
admin.site.index_title = "Origem"