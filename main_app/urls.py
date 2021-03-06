from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('maps/', views.maps_index, name='index'),
    path('maps/<int:map_id>/', views.maps_detail, name='detail'),
    path('maps/create', views.MapCreate.as_view(), name='maps_create'),
    path('maps/<int:pk>/update/', views.MapUpdate.as_view(), name='maps_update'),
path('maps/<int:pk>/delete/', views.MapDelete.as_view(), name='maps_delete'),
]