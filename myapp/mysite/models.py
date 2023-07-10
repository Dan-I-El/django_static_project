from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length = 100)
    details = models.CharField(max_length = 500)

# then use python manage.py makemigrations, migrate, createsuperuser