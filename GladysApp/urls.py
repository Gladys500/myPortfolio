
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about',views.about, name='about'),
    path('starter',views.starter, name='starter'),
    path('contact',views.contact, name='contact'),
    path('portfoliodetails',views.portfolio_details, name='portfolio-details'),
    path('portfolio',views.portfolio, name='portfolio'),
    path('resume',views.resume, name='resume'),
    path('services',views.services, name='services'),
    path('showcontact/' , views.showcontact, name='showcontact'),
    path('delete/<int:id>', views.delete),
]
