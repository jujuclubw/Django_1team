from django.shortcuts import render

# Create your views here.
def Mainfunc(request):
    return render(request,"main.html")  
