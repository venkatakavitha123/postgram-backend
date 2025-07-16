from django.db import models


class User(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=10)
    userName=models.CharField(max_length=20,unique=True)
    dob=models.CharField(max_length=8)
    mobile=models.IntegerField(max_length=10)


    def str(self):
        return self.name
# Create your models here.
