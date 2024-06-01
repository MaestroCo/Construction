from .models import ConstructionOrganization, Area, ConstructionBuilding
from .serializers import ConstructionOrganizationSerializer, AreaSerializer, ConstructionBuildingSerializer
from rest_framework import viewsets, permissions


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user and request.user.is_staff


class ConstructionOrganizationViewSet(viewsets.ModelViewSet):
    queryset = ConstructionOrganization.objects.all()
    serializer_class = ConstructionOrganizationSerializer
    permission_classes = [CustomPermission]


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [CustomPermission]


class ConstructionBuildingViewSet(viewsets.ModelViewSet):
    queryset = ConstructionBuilding.objects.all()
    serializer_class = ConstructionBuildingSerializer
    permission_classes = [CustomPermission]
