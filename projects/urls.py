from rest_framework import routers
from .api import ProjectViewSet
from .api import StudentViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')
router.register('api/students', StudentViewSet, 'students')

urlpatterns = router.urls
