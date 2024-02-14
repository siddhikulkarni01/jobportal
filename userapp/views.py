from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from userapp.forms import usrform,usr_update,usr_img,blogpostform,commentform,subscribeform,userprofile,subscribeform1
from .models import userdetails,User,blogpost,comments,subscribe
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from jobpostdata.models import Jobdata
# Create your views here.

def registration(request):
    registered =False

    if request.method=="POST":
        form= usrform(request.POST)
        profile=userprofile(request.POST,request.FILES)

        if form.is_valid and profile.is_valid :
            user = form.save()
            user.set_password(user.password)
            user.save()

            prof = profile.save(commit=False)
            prof.user = user 
            prof.save()
            registered = True
            return redirect('userapp:login')
    else:
        form = usrform()
        profile = userprofile()

    return render(request,"register.html",{"form":form,"profile":profile,"registered":registered})

def user_login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password =request.POST.get('password')

        user= authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('userapp:home')
            else:
                return HttpResponse(" please check your creds")
        
        else:
            return HttpResponse("please check your creds")
        
    return render(request,"login.html",{})

def index(request):
    return render(request,"index.html")

@login_required(login_url='userapp:login')
def home(request):
    blogposts = blogpost.objects.all().order_by("-view_count")[0:3]
    top_post = blogpost.objects.all().order_by("-view_count")[0]
    newblog =  blogpost.objects.all().order_by("-time")[0:3]
    sub = subscribeform()
    
    saved = False
    error_message = None
    
    if request.method == "POST":
        sub = subscribeform(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['email']
            
            # Check if the email already exists
            if not subscribe.objects.filter(email=email).exists():
                # Save the subscription if the email does not exist
                sub.save()
                saved = True
            else:
                # Set an error message if the email already exists
                error_message = 'This email is already registered.'

    return render(request, "home.html", {"blogposts": blogposts, "sub": sub, "top_post": top_post, "saved": saved, "error_message": error_message,"newblog":newblog})

def user_logout(request):
    logout(request)
    return redirect('userapp:login')

@login_required(login_url='userapp:login')   
def update(request):
    if request.method == "POST":
         form =  usr_update(request.POST,instance=request.user) 
         form1 = usr_img(request.POST, request.FILES, instance=request.user.userdetails)
         if form.is_valid() and form1.is_valid():
             form.save()
             form1.save()
             return redirect('userapp:index')
    else:
        form = usr_update(instance=request.user)
        form1 = usr_img(instance=request.user.userdetails)
    return render(request,"update.html",{"form":form,"form1":form1})

@login_required(login_url='userapp:login')
def user_profile(request):

    userprofile = userdetails.objects.get(user = request.user)

    return render(request,"profile.html",{"userprofile":userprofile})

   

@login_required(login_url='userapp:login')
def ty(request):
    return render(request,"ty.html")

def blogdata(request):
    saved = False

    if request.method == "POST":
        blog_form = blogpostform(request.POST, request.FILES)

        if blog_form.is_valid():
            blog_post = blog_form.save(commit=False)
            blog_post.author_name = request.user
            blog_post.save()
            saved = True
            return redirect('userapp:blog')
        else:
            return HttpResponse("Data was not saved")

    else:
        blog_form = blogpostform()

    return render(request, "blogpost.html", {"blog": blog_form, "saved": saved})

def displayblog(request):

    data = blogpost.objects.all()

    return render(request,"displayblog.html",{"data":data})


def blog(request):
    blog = blogpost.objects.all()
    return render(request,"blog.html",{"blog":blog})

def blogdetail(request, id):
    post = get_object_or_404(blogpost, id=id)
    comment_form = commentform()

    # likes code
    liked = False
    if post.like.filter(id=request.user.id).exists():
        liked = True 
    post_is_liked = liked

    if request.method == "POST":
        comment_form = commentform(request.POST)
        if comment_form.is_valid():
            content = comment_form.cleaned_data['content']
            user = request.user


            post_sno = request.POST.get("postSno")
            print(post_sno)

            parent_sno = request.POST.get("parentSno")

            if parent_sno:
                parent = comments.objects.get(sno=parent_sno)
                comment1 = comments(content=content, user=user, post=post, parent=parent)
            else:
                comment1 = comments(content=content, user=user, post=post)

            comment1.save()

    if post.view_count is None:
        post.view_count = 1
    else:
        post.view_count += 1
    post.save()

    # Ensure that 'post' is defined even if the request method is not POST
    usercomments = comments.objects.filter(post=post).exclude(parent__isnull=False)
   
    reply = comments.objects.filter(post=post, parent__isnull=False)

    recentposts = blogpost.objects.all().order_by("-time")[0:3]
    topposts = blogpost.objects.all().order_by("-view_count")[0:3]

    recentposts_viewmore = blogpost.objects.all().order_by("-time")
    topposts_viewmore = blogpost.objects.all().order_by("-view_count")

    allblog = blogpost.objects.all()

    author_name = post.author_name

    relatedpost= blogpost.objects.exclude(id=id).filter(author_name=author_name)[0:2]

    comment1 = comments.objects.filter(post=post).exclude(parent__isnull=True).count()
    comment2 = comments.objects.filter(post=post).exclude(parent__isnull=False).count()
    total_comment = comment1+comment2
    no_of_likes = post.no_of_like

  

    context = { 'post': post, 
                'form': comment_form,
                'usercomments': usercomments,
                'reply': reply,
                "topposts":topposts,
                "recentposts":recentposts,
                "total_comment":total_comment,
                "rv":recentposts_viewmore,
                "tv":topposts_viewmore,
                "allblog":allblog,
                'post_is_liked':post_is_liked,
                'no_of_likes':no_of_likes,
                'relatedpost':relatedpost,
                
                }
    return render(request, 'blogdetail.html', context)

def likes(request, id):
   
    post_id = request.POST.get('post_id')
    print("post id",post_id)

    post = get_object_or_404(blogpost, id=request.POST.get('post_id'))

   
    if request.user in post.like.all():
        print("Removing like")
        post.like.remove(request.user)
    else:
        print("Adding like")
        post.like.add(request.user)

    return HttpResponseRedirect(reverse('userapp:blogdetails',args=[str(id)]))


def authorview(request, user_id):
    author_details = get_object_or_404(userdetails, user_id=user_id)
    return render(request, "authorview.html", {"author_details": author_details})


def search(request):
    posts = blogpost.objects.all()
    searched = request.GET.get('searched', '')
    blogs = []

    if searched:
        blogs = blogpost.objects.filter(post_title__icontains=searched)
   

    return render(request, "search.html", {"searched": searched, "blogs": blogs, "posts": posts})

def likesdata(request):

    # Retrieve the liked posts for the current user
    liked_posts = blogpost.objects.filter(like=request.user)

    return render(request, "like.html", {"liked_posts": liked_posts})


def bookmark(request, id):

    post = get_object_or_404(blogpost, pk= id)

    if request.user in post.bookmark.all():
        post.bookmark.remove(request.user)
    else:
        post.bookmark.add(request.user)

    return HttpResponseRedirect(reverse('userapp:blogdetails',args=[id]))

def bookmardata(request):

    bk =  blogpost.objects.filter(bookmark=request.user)

    return render(request,"bookmark.html",{"bk":bk})

