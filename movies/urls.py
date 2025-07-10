from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('detalle/<int:id>/', views.movies_details, name='detalle_pelicula'),
]
