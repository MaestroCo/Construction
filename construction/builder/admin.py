from django.contrib import admin
from .models import ConstructionBuilding, ConstructionOrganization, Area


admin.site.register(ConstructionBuilding)
admin.site.register(ConstructionOrganization)
admin.site.register(Area)
