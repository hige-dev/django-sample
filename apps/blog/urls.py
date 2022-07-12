from rest_framework import routers
from .views import UserViewSet, EntryViewSet, get_title
from django.urls import path

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entries', EntryViewSet)

urlpatterns = [
    path(r'get_title', get_title),
]
