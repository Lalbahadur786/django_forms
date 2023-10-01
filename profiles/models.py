from django.db import models

# Create your models here.

class UserProfileModel(models.Model):
    # user_profile = models.FileField(upload_to="image")
    user_profile = models.ImageField(upload_to="image")
