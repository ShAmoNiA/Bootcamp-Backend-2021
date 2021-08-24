import datetime

from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render

from .models import *


# Create your views here.
def pubs_view(request):
    # country = Country.objects.create(name='Iran2')
    # country.save()

    # country = Country.objects.get(name='Iran3')
    # country.name = 'Iran4'
    # country.save()

    # country = Country.objects.get(name='Iran4')
    # country.delete()

    # city = City.objects.get(name='Los Angele')
    # iran_country = Country.objects.get(name='Iran')
    # city.country = iran_country
    # city.save()

    # author = Author.objects.get(last_name='Dolat Abadi')
    # book = Book.objects.get(book_name='Book3')
    # author.books.add(book)
    # book.save()

    # queryset = Book.objects.all()
    # publisher = Publisher.objects.get(publisher_id=1)
    # queryset = Book.objects.filter(publisher__publisher_name='Sarmad')
    # queryset = Store.objects.filter(city__country__name='Iran')
    queryset = Book.objects.filter(book_name__icontains=F('publisher__publisher_name'))

    # for item in queryset:
    #     print(item.book_name)
    return HttpResponse(queryset)

