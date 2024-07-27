from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # Esto consulta todos los datos
    permission_classes = [permissions.AllowAny] # Con esto indicamos que cualquier cliente puede pedir datos al servidor
    serializer_class = ProjectSerializer