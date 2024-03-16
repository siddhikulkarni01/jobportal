from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from jobpostdata.models import Jobdata,applyjobs
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from jobpostdata.forms import applyuser
from django.shortcuts import render, get_object_or_404

# Create your views here.

@login_required(login_url='userapp:login')   
def jobdetails(request):

    jobs = Jobdata.objects.all()
    return render(request,"jobpost/jobdetails.html",{"jobs":jobs})


def job_display(request, pk):
    details = get_object_or_404(Jobdata, pk=pk)
    return render(request, 'jobpostdata/Jobdata_detail.html', {'details': details})

# class JobDisplay(DetailView):

#     context_object_name = "details"

#     model = Jobdata


@login_required(login_url='userapp:login')
def applyuserapp(request):
    jobdata = Jobdata.objects.all()

    if request.method == 'POST':
        formuser = applyuser(request.POST, request.FILES)
        formuser.instance.user = request.user  # Assign the current user to the job application

        # Extract the selected jobtitle from the form data
        selected_jobtitle_id = request.POST.get('jobtitle')
        
        # Set the jobtitle in the instance based on the selected jobtitle ID
        if not formuser.instance.jobtitle:
            # Set a default job title based on some logic or condition
            default_jobtitle = Jobdata.objects.get(name='jobtitle')
            formuser.instance.jobtitle = default_jobtitle
            
        if formuser.is_valid():
            formuser.save()
            return redirect('userapp:ty')
    else:
        formuser = applyuser()

    return render(request, "apply.html", {"formuser": formuser, "jobdata": jobdata})



def appliedjobs(request):

    userjobs = applyjobs.objects.filter(user=request.user).select_related('jobtitle')

    print(userjobs)
    
    return render(request,"appliedjobs.html",{"userjobs":userjobs})

# bk =  blogpost.objects.filter(bookmark=request.user)

#     return render(request,"bookmark.html",{"bk":bk})