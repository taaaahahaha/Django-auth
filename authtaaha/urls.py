from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('about', views.about, name='about'),
    path('signup', views.signup, name='signup'),
    path('details', views.details, name='details'),
    path('logout',views.logout_view,name='logout'),
    path('editpass/<str:username>',views.editpass,name='editpass'),
    path('edituname/<str:username>',views.edituname,name='edituname'),
    path('editemail/<str:username>',views.editemail,name='editemail'),
    path('editadd/<str:username>',views.editadd,name='editadd'),
    path('delete/<str:username>',views.delete,name='delete'),

]
