from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage),
    path('counttheword/', views.count, name ="count"),
]
