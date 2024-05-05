from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .custom import *

# Create Router object
router = DefaultRouter()

# Register viewset with Router
router.register(r"items", ItemViewSet, basename="item")
router.register(r"modelitems", ItemModelViewSet, basename="modelitem")
router.register(r"readOnlyMVitems", ItemReadOnlyMVSet, basename="readOnlyMVitem")

# router.register(r"items", ItemGenericViewSet)


# Add router url in url patterns
urlpatterns = [
    path("", include(router.urls)),
    path("testing_api/", testing_api),
    path("post_testing_api/", post_testing_api),
    path("update_testing_api/", update_testing_api),
    path("delete_testing_api/", delete_testing_api),
]
