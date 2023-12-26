from django.db import models

# Create your models here.


class Register_Table(models.Model):
    firstname = models.CharField(max_length=155)
    lastname = models.CharField(max_length=155)
    email = models.EmailField(max_length=155)
    phone = models.CharField(max_length=10)
