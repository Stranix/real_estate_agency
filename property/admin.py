from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnersFlatsInLine(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('flat', 'owner')


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = (
        'town',
        'address',
        'owner',
    )
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town'
    )
    inlines = [OwnersFlatsInLine]
    list_filter = (
        'new_building',
        'rooms_number',
        'has_balcony',
    )
    raw_id_fields = ('liked_by',)
    list_editable = ('new_building',)
    readonly_fields = ('created_at',)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = (
        'author',
        'flat',
    )


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'pure_phone', 'phonenumber')
    raw_id_fields = ('flats',)
