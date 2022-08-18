from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    qrcode=models.ImageField(upload_to='qr_code_images',default='blank-profile-picture.png')
    city = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=10,blank=True)
    token= models.CharField(max_length=255, blank=True,default='blank')

