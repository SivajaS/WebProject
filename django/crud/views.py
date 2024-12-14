from django.shortcuts import render,redirect
from .models import Register
from .forms import RegisterForm
from django.contrib.auth.models import User #for signup
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as authlogin,authenticate#change the module name
from django.contrib.auth import logout as authlogout
# Create your views here.
def home(request):
    data=Register.objects.all()
    return render(request,'home.html',{'data':data})
    
def register(request,id=0):
    if request.method == "GET":
        if id == 0:
            frm = RegisterForm()
        else:
            frm = Register.objects.get(pk=id)
            frm = RegisterForm(instance = frm)
        return render(request, "register.html", {'frm': frm})
    else:
        if id == 0:
            frm = RegisterForm(request.POST)
        else:
            frm = Register.objects.get(pk=id)
            frm = RegisterForm(request.POST,instance = frm)
        if frm.is_valid():
            frm.save()
        return redirect('/')
    
@login_required(login_url='login/')#always on the applied function top    
def delete(request,id):
    delete_data=Register.objects.get(pk=id)
    delete_data.delete()
    return redirect('/')

def login(request):
    error_message=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            authlogin(request,user)
            return redirect('home')#function name
        else:
            error_message="INVALID CERDENTIALS"
    return render(request,'login.html',{'error_message':error_message})

def logout(request):
    authlogout(request)
    return redirect('login')

def signup(request):
    user=None
    error_messsage=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        # print(username,password)
        try:
            user=User.objects.create_user(username=username,password=password)
        except Exception as e:
            error_messsage=str(e)    
    return render(request,'signup.html',{'user':user,'error_message':error_messsage})