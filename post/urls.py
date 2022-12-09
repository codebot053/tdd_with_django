from django.urls import path
from post import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
]
