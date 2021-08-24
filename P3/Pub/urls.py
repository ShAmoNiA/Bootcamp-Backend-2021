from django.urls import path, include

from Pub.views import pubs_view

app_name = 'Pub'
urlpatterns = [
    path('api/', pubs_view, name='pub-api'),
]
