from django.conf.urls import url
from django.urls import path
from django.urls.conf import include
from .views import Home,Sites
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'sites', Sites, basename='user')

urlpatterns = [
    path('<int:x>/<int:y>', Home),
]
urlpatterns+=router.urls
