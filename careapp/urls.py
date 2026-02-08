
from django.contrib import admin
from django.urls import path
from careapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('service-details/', views.service_details, name='service_details'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('department/', views.department, name='department'),

    path('doctor/', views.doctor, name='doctor'),

    
    path('contact/', views.contact, name='contact'),

    path('appointment/', views.Appoint, name='appointment'),
    
    path('show/', views.show, name='show'),

    path('delete/<int:id>', views.delete ),
    
    path('edit/<int:id>', views.edit ),

    path('', views.register, name='register'),
    
    path('login/', views.login_user, name='login'),


]
