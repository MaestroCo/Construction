from rest_framework import serializers

from .models import Area, ConstructionBuilding, ConstructionOrganization


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


class ConstructionBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionBuilding
        fields = '__all__'


class ConstructionOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionOrganization
        fields = '__all__'