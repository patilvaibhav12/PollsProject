from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('create/', views.create, name="create"),
    path('vote/', views.vote, name='vote'),
    #path('results/', views.results, name='results'),
    path('results/<poll_id>/', views.results, name='results'),
    
]