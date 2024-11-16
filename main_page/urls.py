from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('main_page/upload/', views.upload_csv, name='upload_csv'),
]