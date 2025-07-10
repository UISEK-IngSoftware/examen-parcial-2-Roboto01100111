from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
app_name = "api"
router = DefaultRouter()
router.register(r'movies', views.GoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
