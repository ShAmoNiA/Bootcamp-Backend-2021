from django.contrib import admin

# Register your models here.
from Pub.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'category_name', 'description']
    search_fields = ['category_name', 'description']
    list_filter = ['category_name']

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_display = ['country_id', 'name']
    search_fields = ['name']

    class Meta:
        model = Country


admin.site.register(Country, CountryAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ['city_id', 'name', 'country_name']
    search_fields = ['name']
    list_filter = ['country']

    def country_name(self, obj):
        result = Country.objects.get(country_id=obj.country.country_id)
        return result.name

    class Meta:
        model = City


admin.site.register(City, CityAdmin)


class StoreAdmin(admin.ModelAdmin):
    list_display = ['store_id', 'store_name']
    search_fields = ['store_name']
    list_filter = ['country']

    class Meta:
        model = Store


admin.site.register(Store, StoreAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author_id', 'full_name', 'is_active']
    search_fields = ['first_name', 'last_name']
    list_filter = ['is_active']

    def full_name(self, obj):
        return obj.__str__()

    class Meta:
        model = Author


admin.site.register(Author, AuthorAdmin)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['publisher_id', 'publisher_name', 'date_established']
    search_fields = ['publisher_name']
    list_filter = ['category']

    class Meta:
        model = Publisher


admin.site.register(Publisher, PublisherAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['book_id', 'book_name', 'publisher_name', 'date_published', 'price']
    list_filter = ['publisher']

    def publisher_name(self, obj):
        result = Publisher.objects.get(publisher_id=obj.publisher.publisher_id)
        return result.publisher_name

    class Meta:
        model = Book


admin.site.register(Book, BookAdmin)
