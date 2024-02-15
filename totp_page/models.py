from django.db import models

# Create your models here.
class TOTPCode(models.Model):
    federation = models.CharField(max_length=50, blank = True)
    role = models.CharField(max_length=50, blank = True)
    code = models.CharField(max_length=50, blank = True)
    