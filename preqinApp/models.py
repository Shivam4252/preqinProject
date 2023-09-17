# randomfloatapp/models.py
from django.db import models

class RandomFloatGenerator(models.Model):
    input_string = models.CharField(max_length=1200)
    random_value = models.FloatField()
