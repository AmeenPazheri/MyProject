from django.shortcuts import render, get_object_or_404, redirect
from .models import  User,Vehicle
from django.contrib import messages, auth
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth import login as auth_login,logout
from django.contrib.auth.decorators import login_required

def login(request):
    error=''
    if request.POST:
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if request.GET.get("next"):
                return redirect(request.GET.get("next"))
            return redirect("/")
        else:
            error = "Incorrect Username or password"
    context = {"error": error}
    return render(request, "login.html",context)


def registration(request):
    if request.method=='POST':
        email = request.POST['email']
        user_type=request.POST['user_type']
        password = request.POST['password']
        password1 = request.POST['confirm_password']
        if password==password1:

            if User.objects.filter(email=email).exists():

                messages.info(request,'email exist')
                return render(request,'registraion.html')
            else:

                if user_type=='S':
                    User.objects.create_superuser(password=password,email=email)
                elif user_type=='A':
                    User.objects.create_admin_user(password=password, email=email)
                else:
                    User.objects.create_user(password=password, email=email)
                return redirect('/login/')
        else:
            messages.info(request,'password not matching')
        return render(request,'registraion.html')
    return render(request,'registraion.html')



def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url="vehapp:login")
def Vehicle_list(request):
    Vehicles=Vehicle.objects.all()
    context = {
        "Vehicles": Vehicles,
    }
    return render(request, "vehicle_list.html", context)

@login_required(login_url="vehapp:login")
def Vehicle_Create(request):
    error = ''
    if request.method == 'POST':
        if request.user.user_type=='S':
            vehicle_number = request.POST.get('vehicle_number', '')
            vehicle_type= request.POST.get('vehicle_type', '')
            vehicle_model= request.POST.get('vehicle_model', '')
            vehicle_description= request.POST.get('vehicle_description', '')
            vehicle= Vehicle(vehicle_number=vehicle_number, vehicle_type=vehicle_type, vehicle_model=vehicle_model,vehicle_description=vehicle_description)
            vehicle.save()
        else:
            error = "You are not autherised "
    context = {"error": error}

    return render(request, 'create.html',context)


@login_required(login_url="vehapp:login")
def Vehicle_RUD(request,id):
    error=''
    vehicle=Vehicle.objects.get(id=id)
    if request.user.user_type == 'S' or request.user.user_type == 'A':
        vehicle_number = request.POST.get('vehicle_number', '')
        vehicle_type = request.POST.get('vehicle_type', '')
        vehicle_model = request.POST.get('vehicle_model', '')
        vehicle_description = request.POST.get('vehicle_description', '')
        vehicle.vehicle_number=vehicle_number
        vehicle.vehicle_type = vehicle_type
        vehicle.vehicle_model = vehicle_model
        vehicle.vehicle_description = vehicle_description
        vehicle.save()
    else:
        error = "You are not autherised "

    context = {
        "vehicle": vehicle,"error": error
    }
    return render(request, "update.html", context)

@login_required(login_url="vehapp:login")
def delete_view(request,id):
    message=''
    if request.user.user_type == 'S':
        Vehicle.objects.get(id=id).delete()
        message = 'Deleted Successfuly'
    else:
        message='Not Authorized for delete'
    context={"error":message}
    return redirect('/')






