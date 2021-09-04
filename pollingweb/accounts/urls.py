from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register.html'),
    path('login/', views.login, name = 'login.html'),
    path('logout/', views.logout, name = 'logout.html'),
    #path("dataupdate/", views.dataupdate, name="dataupdate.html"),
    path("profile",views.profile,name="profile"),
    path('deletep/<poll_id>/', views.deletep, name='deletep'),
]