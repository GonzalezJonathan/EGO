from rest_framework import routers
from .api import AutoViewset

router = routers.DefaultRouter()

router.register('api/autos', AutoViewset, 'autos')

urlpatterns = router.urls