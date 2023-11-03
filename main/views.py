from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import ToRegion

# Create your views here.

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been log in")
            return redirect('home')
        else:
            messages.success(request, "there was an error logging in!")
            return redirect('home')
    else:
        return render(request, 'home.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logout!")
    return redirect('home')

def inout(request):
    records = ToRegion.objects.all()
    return render(request,'inout.html',{'records': records})
