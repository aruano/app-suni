from django.conf.urls import url
from .models import Escuela
from .views import *

urlpatterns = [
    url(r'^add/', EscuelaCrear.as_view(), name='escuela_crear'),
]