from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('download/<resolution>', views.download, name='download')
]