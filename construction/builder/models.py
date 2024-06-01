from django.db import models


class Area(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ConstructionOrganization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    organized = models.DateTimeField(auto_now_add=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ConstructionBuilding(models.Model):
    organization = models.ForeignKey(ConstructionOrganization, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    field = models.IntegerField()
    floor = models.IntegerField()
    parking = models.BooleanField(default=False)
    playground = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
