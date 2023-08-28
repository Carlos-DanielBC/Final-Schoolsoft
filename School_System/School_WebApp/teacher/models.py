from django.db import models

# Create your models here.
class Teachers(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    code = models.IntegerField()
    id_number = models.CharField('cedula',max_length=11)
    
