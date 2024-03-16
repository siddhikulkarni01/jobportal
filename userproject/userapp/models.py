from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from timezone_field import TimeZoneField
from django.utils.text import slugify

# Create your models here.
class userdetails(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_img=models.ImageField(upload_to='userimages/',blank=True, default='userimages/image.png')
    address =models.CharField(max_length=200,blank=True)
    linkedin = models.CharField(max_length=200,blank=True)
    facebook = models.CharField(max_length=200,blank=True)
    instagram = models.CharField(max_length=200,blank=True)
    twitter = models.CharField(max_length=200,blank=True)
    time_zone = TimeZoneField(default='Asia/Kolkata')

    def __str__(self) -> str:
        return str(self.user)



class blogpost(models.Model):

    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=200)
    post_title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=100,blank=True,null=True)
    description= models.TextField(max_length=10000)
    image = models.ImageField(upload_to='blogimages/',blank=True)
    time = models.DateTimeField(auto_now_add=True)
    view_count =  models.IntegerField(blank=True,null=True)
    time_zone = TimeZoneField(default='Asia/Kolkata')
    like = models.ManyToManyField(User,related_name="postlikes")
    bookmark = models.ManyToManyField(User, related_name="bookmarks")

    def __str__(self):
        return self.post_title
    
    def no_of_like(self):
        return self.like.count()
   
  


class comments(models.Model):

    sno = models.AutoField(primary_key=True)
    content = models.TextField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True,null=True)
    post = models.ForeignKey(blogpost, related_name="postdata", on_delete=models.CASCADE)
    parent =  models.ForeignKey('self' ,null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    time_zone = TimeZoneField(default='Asia/Kolkata')

    def __str__(self):
        return str(self.user)

class subscribe(models.Model):

    email= models.EmailField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    