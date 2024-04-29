from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, ItemModelViewSet, ItemReadOnlyMVSet

# Create Router object
router = DefaultRouter()

# Register viewset with Router
router.register(r'items',ItemViewSet,basename='item')
router.register(r'modelitems', ItemModelViewSet, basename='modelitem')
router.register(r'readOnlyMVitems', ItemReadOnlyMVSet, basename='readOnlyMVitem')


# Add router url in url patterns
urlpatterns = router.urls