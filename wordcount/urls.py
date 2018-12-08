from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage),
    path('countthe/', views.count, name ="counter"),
]
