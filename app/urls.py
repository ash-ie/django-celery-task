from django.urls import path

from app import views

urlpatterns = [
    path('', views.test_view,name='test_view'),
]