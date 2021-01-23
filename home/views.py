from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Login
from home.models import Signup

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('this is home page')

def about(request):
     return render(request, 'about.html')

def services(request):
     return render(request, 'services.html')

def contact(request):
     if request.method == "POST":
          name= request.POST.get('name')
          email= request.POST.get('email')
          phone= request.POST.get('phone')
          desc= request.POST.get('desc')
          contact= Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
          contact.save()

     return render(request, 'contact.html')

def login(request):
     if request.method == "POST":
          username= request.POST.get('username')
          password= request.POST.get('password')
          login=Login(username=username, password=password, date= datetime.today())
          login.save()

     return render(request, 'login.html')

def signup(request):
     if request.method == "POST":
          username= request.POST.get('username')
          email= request.POST.get('email')
          password= request.POST.get('password')
          confirmpassword= request.POST.get('confirmpassword')
          phone= request.POST.get('phone')
          signup=Signup(username=username,email=email, password=password,confirmpassword=confirmpassword, phone=phone, date= datetime.today())
          signup.save()

     return render(request, 'signup.html')

def view(request):
     return render(request, 'about.html')

   