from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import ToRegion, FromRegion
from .forms import ToRegionForm


# Create your views here.

def home(request):
    if request.method == 'POST':
        if "loginbtn" in request.POST:
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
    fromrecords = FromRegion.objects.all() 
    if request.method == 'POST':
        try:
            formToRegion = ToRegionForm(request.POST)
            if "saveToRegion" in request.POST:
                if formToRegion.is_valid():
                    formToRegion.save()
                    messages.success(request, 'You have add record')
                    return redirect('inout')
                else:
                    messages.success(request, 'error not valid')
                    print(f'Form Errors: {formToRegion.errors}')
                    return render(request,'inout.html',{'records': records, 'fromrecords': fromrecords})                    
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')

    return render(request,'inout.html',{'records': records, 'fromrecords': fromrecords})
    

def addToRegion(request):
    return render(request,'addToRegion.html',{})

def addFromRegion(request):
    return render(request,'addFromRegion.html',{})

def deleteTo(request, pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            deleteTo = ToRegion.objects.get(id=pk)
            deleteTo.delete()
            messages.success(request, 'You successfuly deleted a record')
            return redirect('inout')
        else:
            deleteIt = get_object_or_404(ToRegion, pk=pk)
            context = {'deleteIt': deleteIt}
            return render(request,'confirmDelete.html',context)