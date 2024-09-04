from django.db import models
from django.contrib.auth.models import AbstractUser


# For registration we are taking first_name, 
# last_name, email, phone_no, date_of_birth, city, country, pincode
# password and confirm passsword, 
# Abstract user has already first_name, last_name, email so no need to make that in this class
class UserRegisterModel(AbstractUser):
    username = ['email']
    phone_no = models.CharField(max_length=13, unique= True)   # with country code 
    date_of_birth = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    pincode = models.BigIntegerField()
    profile_pic = models.URLField()   # from front end user will upload the pic and store it AWS s3 bucket 
                                    #  than we will take url from fe

    password = models.CharField(max_length=15)
    confirm_password = models.CharField(max_length=15)










