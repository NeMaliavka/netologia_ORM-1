from django.urls import path
from .views import catalog, phone_detail

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('catalog/<slug:slug>/', phone_detail, name='phone_detail'),
]
