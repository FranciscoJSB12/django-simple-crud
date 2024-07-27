from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects') # El último parámetro es el nombre de la ruta

urlpatterns = router.urls
