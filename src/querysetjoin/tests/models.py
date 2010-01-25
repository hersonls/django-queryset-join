from django.db import models

class ModelOne(models.Model):
    name = models.CharField(max_length=100)
    work = models.CharField(max_length=100)

    class Meta:
        app_label = "querysetjoin"

class ModelTwo(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)

    class Meta:
        app_label = "querysetjoin"