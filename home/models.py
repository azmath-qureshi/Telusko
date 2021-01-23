from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=22)
    email=models.CharField(max_length=142)
    phone=models.CharField(max_length=10)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.email

class Login(models.Model):
    username=models.CharField(max_length=22)
    password=models.CharField(max_length=22)
    date=models.DateField()

    def __str__(self):
        return self.username

class Signup(models.Model):
    username=models.CharField(max_length=22)
    email=models.CharField(max_length=142)
    password=models.CharField(max_length=22)
    confirmpassword=models.CharField(max_length=22)
    phone=models.CharField(max_length=10)
    birthday=models.CharField(max_length=10)
    date=models.DateField()

    def __str__(self):
        return self.email   