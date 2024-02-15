from django.db import models

# Create your models here.
class TOTPCode(models.Model):
    federation = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    