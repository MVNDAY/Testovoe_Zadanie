from django.db import models 
from django.contrib.auth.models import User

# Create your models here.

class Counter(models.Model):
	counter_value = models.IntegerField(default = 0)


