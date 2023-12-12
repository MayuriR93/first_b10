from django.shortcuts import render, HttpResponse
from .models import Employee

# Create your views here.

# def homepage(request):
#     print(request.method, request.user)
#     return HttpResponse("Hello")   #------- ya home page sathi url define karaw lagel urls.py file madhe

def homepage(request):
    # print(request.method, request.user)
    emps = Employee.objects.all()
    return render(request, "home.html",context={"name":["Mayank", "Mayuri", "Likhesh", "Sakshi"], "all_emps": emps})   #---- jevha aapan url hit karto tyanantr homepage call hot tyanantr html page render karto aani html page madhe aapan sobat {"name":"Mayank"} hi dict. gheun jato