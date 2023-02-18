from django.contrib import admin
from sortir.models import *

class SortirAdmin(admin.ModelAdmin):
    list_display = ['barcode', 'scanner', 'created_at',]
    search_fields = ['barcode', 'scanner', 'created_at',]
    list_filter = ('scanner', 'created_at')
    list_per_page = 10

class DoubleAdmin(admin.ModelAdmin):
    list_display = ['barcode', 'scanner', 'created_at',]
    search_fields = ['barcode', 'scanner', 'created_at',]
    list_filter = ('scanner', 'created_at')
    list_per_page = 10

# class SdayAdmin(admin.ModelAdmin):
#     list_display = ['jumlah',]
#     search_fields = ['jumlah',]
#     list_per_page = 10
# class DdayAdmin(admin.ModelAdmin):
#     list_display = ['jumlah',]
#     search_fields = ['jumlah',]
#     list_per_page = 10

# class ScannerAdmin(admin.ModelAdmin):
#     list_display = ['name']


admin.site.register(Sortir, SortirAdmin)
admin.site.register(Double, DoubleAdmin)
# admin.site.register(Dday, DdayAdmin)
# admin.site.register(Sday, SdayAdmin)
# admin.site.register(Scanner, ScannerAdmin)

admin.site.site_header = 'Antarestar'
admin.site.site_title = "Gudang Antares"
admin.site.index_title = "Antarestar Admin"