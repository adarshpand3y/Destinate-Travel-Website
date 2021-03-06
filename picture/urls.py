from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('images', views.images),
    path('image/<str:pk>', views.image),
    path('member/<str:mem_id>', views.member),
    path('team', views.team),
    path('search', views.search),
    path('contact', views.contact)
]
