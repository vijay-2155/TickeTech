from django.contrib import admin
from .models import City, Museum, MuseumImage, Price, Category, Ticket


# Inline model to add images directly in the Museum admin panel
class MuseumImageInline(admin.TabularInline):
    model = MuseumImage
    extra = 1  # Number of extra empty forms displayed


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Museum)
class MuseumAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name', 'city__name')
    list_filter = ('city',)
    inlines = [MuseumImageInline]  # Add the MuseumImage inline form to Museum admin


@admin.register(Ticket)

class TicketAdmin(admin.ModelAdmin):
   pass

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('price', 'category')
    search_fields = ('price', 'category')
    list_filter = ('category',)
    inlines = [MuseumImageInline]
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    inlines = [MuseumImageInline]
