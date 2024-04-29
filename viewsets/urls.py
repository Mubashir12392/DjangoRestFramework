from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

# Create Router object
router = DefaultRouter()

# Register viewset with Router
router.register(r'items',ItemViewSet,basename='item')

# Add router url in url patterns
urlpatterns = router.urls