
from .models import  department,course,Application
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import ApplicationForm

def index(request):
    return render(request,'index.html')

def courses(request):
    return render(request,'courses.html')


def application_form(request):
    depobj = department.objects.all()
    courseobj = course.objects.all()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            print(form)
            success_message = "Order confirmed. <a href='{}'>Return to home page</a>".format(reverse("storeapp:index"))

            messages.success(request, success_message, extra_tags='safe')
            return redirect('/success/')
    else:
        form = ApplicationForm()
    return render(request, 'application_form.html', {'form': form,'depdata':depobj,'coursedata':courseobj})

def success_view(request):
    message = 'Order confirmed.'
    return render(request, 'success.html', {'message': message})

def saved_forms(request):
    saved_forms =ApplicationForm.objects.all()
    context = {'saved_forms': saved_forms}
    return render(request, 'saved.html', context)
