from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,"service.html")

def movingtips(request):
    return render(request,"movingtips.html")

def workgallery(request):
    return render(request,"workgallery.html")

def contact(request):
    return render(request,"contact.html")

def enquiry(request):
    return render(request,"enquiry.html")