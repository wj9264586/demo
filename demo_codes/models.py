from django.db import models

# Create your models here.
class Staff(models.Model):
    SEX= (
        (0,"男"),
        (1,"女")
    )
    username = models.CharField(
        max_length=255
    )
    age = models.CharField(
        max_length=255
    )
    sex = models.IntegerField(
        choices=SEX
    )