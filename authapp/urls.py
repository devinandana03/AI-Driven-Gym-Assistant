from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('contact',views.contact,name="contact"),
    path('join',views.enroll,name="enroll"),
    path('profile',views.profile,name="profile"),
    path('gallery',views.gallery,name="gallery"),
    path('attendance',views.attendance,name="attendance"),
    path('biceps/', views.biceps_pose, name='biceps_pose'),
    path('benchpress/', views.benchpress, name='benchpress'),
    path('chest/', views.chest, name='chest'),
    path('lateralraise/', views.lateralraise, name='lateralraise'),
    path('squats/', views.squats, name='squats'),
    path('legraise/', views.legraise, name='legraise'),
    path('shoulderpress/', views.shoulderpress, name='shoulderpress'),
 # URL for biceps pose

    
]
