from django.contrib import admin
from userapp.models import userdetails,blogpost,comments
from jobpostdata.models import applyjobs,Jobdata

# Register your models here.
admin.site.register(Jobdata)
admin.site.register(userdetails)
admin.site.register(applyjobs)
admin.site.register(blogpost)
admin.site.register(comments)