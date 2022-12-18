from rest_framework import routers
from .api import ProjectViewSet
from .api import StudentViewSet
from .api import GradeViewSet
from .api import ProfessorViewSet
from .api import FacultyViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')
router.register('api/students', StudentViewSet, 'students')
router.register('api/grades', GradeViewSet, 'grades')
router.register('api/professors', ProfessorViewSet, 'professors')
router.register('api/faculties', FacultyViewSet, 'faculties')

urlpatterns = router.urls
