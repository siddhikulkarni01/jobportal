from django.urls import path
from jobpostdata import views


app_name = 'jobpostdata'


urlpatterns = [
    path('',views.jobdetails,name="jobdetails"),
    path('apply/<int:pk>/',views.applyuserapp,name="apply"),
    path('<int:pk>/', views.job_display, name='job_display'),
    path('appliedjobs/',views.appliedjobs, name="appliedjobs"),
   
    


    

]