
from . import views
from django.urls.conf import path


urlpatterns = [
    path("factorial/", views.factorial_view),
]