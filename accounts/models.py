from django.db import models

# Create your models here.
# DATA BASE 

class profile(models.Model):

   user = models.OneToOneField(User, on_delete=models.CASCADE)
   