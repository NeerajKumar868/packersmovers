from django.urls import path
from .views import *
from.import views



urlpatterns=[
    path('home/',views.index,name="index"),
    path('about-us/',views.about,name="about"),
    path('service/',views.service,name="service"),
    path('moving-tips/',views.movingtips,name="movingtips"),
    path('work-gallery/',views.workgallery,name="workgallery"),
    path('contact-us/',views.contact,name="contact"),
    path('enquiry-us/',views.enquiry,name="enquiry")
]