from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_list, name='about_list'),
    path('about/create/', views.about_create, name='about_create'),
    path('about/update/<int:pk>/', views.about_update, name='about_update'),
    path('about/delete/<int:pk>/', views.about_delete, name='about_delete'),


    path('', views.about_list, name='experience_list'),
    path('experience/create/', views.about_create, name='experience_create'),
    path('experience/update/<int:pk>/', views.about_update, name='experience_update'),
    path('experience/delete/<int:pk>/', views.about_delete, name='experience_delete'),

    path('', views.about_list, name='education_list'),
    path('education/create/', views.about_create, name='education_create'),
    path('education/update/<int:pk>/', views.about_update, name='education_update'),
    path('education/delete/<int:pk>/', views.about_delete, name='education_delete'),

    path('', views.about_list, name='contact_list'),
    path('contact/create/', views.about_create, name='contact_create'),
    path('contact/update/<int:pk>/', views.about_update, name='contact_update'),
    path('contact/delete/<int:pk>/', views.about_delete, name='contact_delete'),


]
