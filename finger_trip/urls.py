"""finger_trip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from trip import views
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Finger Trip Admin"
admin.site.site_title = "Finger Trip Admin Panel"
admin.site.index_title = "Welcome to Finger Trip Admin Panel!"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('search/', views.search, name="search"),
    path('contact/', views.contact, name="contact"),
    path('wall/', views.wall, name="wall"),
    path('wall/<int:trip_id>', views.trip_detail, name="trip_detail"),

    #Like and comment
    path('like/', views.like_post, name="like_post"),
    #path('wall/trip/<int:trip_id>/comment', views.comment_post, name="comment_post"),

    #uploading
    path('create/', views.createuploads, name="createuploads"),
    path('current/', views.currentuploads, name="currentuploads"),
    path('trip/<int:trip_pk>', views.viewtrip , name="viewtrip"),
    path('trip/<int:trip_pk>/delete', views.deletetrip, name="deletetrip"),

    #Auth
    path('signup/', views.signupuser, name="signupuser"),
    path('logout/', views.logoutuser, name="logoutuser"),
    path('login/', views.loginuser, name="loginuser"),

]

#adding MEDIA_URL and MEDIA_ROOT
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
