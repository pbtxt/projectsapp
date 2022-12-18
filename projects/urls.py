from rest_framework import routers
from .api import ProjectViewSet
from .api import StudentViewSet
from .api import GradeViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')
router.register('api/students', StudentViewSet, 'students')
router.register('api/grades', GradeViewSet, 'grades')

urlpatterns = router.urls
