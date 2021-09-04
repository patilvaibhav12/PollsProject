from django.db import models

# Create your models here.
class Userdata(models.Model):
    username = models.CharField(max_length=100,default = '')
    fullname = models.CharField(max_length=150, default = '')
    email = models.CharField(max_length=150, default = '')
    ifsc = models.CharField(max_length=50, default = '')
    phoneno = models.CharField(max_length=20)

    def __str__(self):
        return self.username