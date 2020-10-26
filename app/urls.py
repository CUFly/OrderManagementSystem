from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexpage),
    path('home/', views.homepage, name='homepage'),
    path('create/', views.create, name='create'),

    path('updateorder/<str:pk>/', views.updateorder, name='updateorder'),
    path('deleteorder/<str:pk>/', views.deleteorder, name='deleteorder'),
]