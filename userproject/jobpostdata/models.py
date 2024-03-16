from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from userapp.models import  userdetails


# Create your models here.
class Jobdata(models.Model):
    
    job_title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    company = models.CharField(max_length=100)
    posted_on = models.DateTimeField()
    location = models.CharField(max_length=100)
    salary = models.IntegerField()
    type = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.job_title
    
    

class applyjobs(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    jobtitle = models.ForeignKey(Jobdata,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    pg = models.CharField(max_length=100,null=True,blank=True)
    degree = models.CharField(max_length=100)
    PU = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    resume = models.ImageField(upload_to='resume/' ,blank=True)
    
    def __str__(self):
        return self.first_name
    
 