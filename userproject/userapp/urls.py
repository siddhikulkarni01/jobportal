from django.urls import path
from userapp import views

app_name = 'userapp'

urlpatterns = [
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('login/',views.user_login,name="login"),
    path("registration/",views.registration,name="registration"),
    path('logout/',views.user_logout,name='logout'),
    path('update/',views.update,name="update"), 
    path('profile/',views.user_profile,name="profile"),
    path('ty/',views.ty,name="ty"),
    path("blogpost/",views.blogdata,name="blogpost"),
    path("blog/",views.blog,name="blog"),
    path("blogdetails/<int:id>/",views.blogdetail,name="blogdetails"),
    path("authordata/<int:user_id>/",views.authorview,name="author"),
    path("search/",views.search,name="search"),
    path("likes/<int:id>/",views.likes,name="likes"),
    path("likedata/",views.likesdata,name="likedata"),
    path('bookmark/<int:id>/', views.bookmark, name='bookmark'),
    path("bookmarkdata/",views.bookmardata,name="bookmarkdata"),

]