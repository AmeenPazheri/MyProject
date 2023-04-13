from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/new/')
        else:
            messages.info(request,'invalid credentials')
            return render(request,'login.html')
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username exist')
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email exist')
                return render(request,'register.html')
            else:
                user=User.objects.create_user(username=username,password=password,email=email)
                user.save();
                return redirect('/credentials/login/')
        else:
            messages.info(request,'password not matching')
        return render(request,'register.html')
    return render(request,'register.html')