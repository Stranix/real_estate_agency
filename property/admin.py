from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = (
        'town',
        'address',
        'owner',
    )
    list_display = (
        'address',
        'owner_pure_phone',
        'owners_phonenumber',
        'price',
        'new_building',
        'construction_year',
        'town'
    )
    list_filter = (
        'new_building',
        'rooms_number',
        'has_balcony',
    )
    raw_id_fields = ('like_by',)
    list_editable = ('new_building',)
    readonly_fields = ('created_at',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'author',
        'flat',
    )


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
