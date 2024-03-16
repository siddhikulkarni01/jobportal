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
 # Assuming applyuser is a Django form defined in forms.py

def applyuserapp(request, pk):
    instance = get_object_or_404(applyjobs, pk=pk)
    if request.method == 'POST':
        form = applyuser(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect to a thank you page upon successful update
    else:
        form = applyuser(instance=instance)
    return render(request, 'applyjob_form.html', {'form': form,'instance':instance})


def appliedjobs(request):

    userjobs = applyjobs.objects.filter(user=request.user).select_related('jobtitle')

    print(userjobs)
    
    return render(request,"appliedjobs.html",{"userjobs":userjobs})

# bk =  blogpost.objects.filter(bookmark=request.user)

#     return render(request,"bookmark.html",{"bk":bk})


