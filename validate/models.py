from django.db import models

# Create your models here.

# Modelo para guardar el documento

class FileModel(models.Model):
	
	file = models.FileField(upload_to='documents/')