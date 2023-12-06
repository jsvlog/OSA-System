from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import ToRegion, FromRegion
from .forms import ToRegionForm, FromRegionForm


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
            formFromRegion = FromRegionForm(request.POST)
            if "saveToRegion" in request.POST:
                if formToRegion.is_valid():
                    formToRegion.save()
                    messages.success(request, 'You have add record')
                    return redirect('inout')
                else:
                    messages.success(request, 'error not valid')
                    print(f'Form Errors: {formToRegion.errors}')
                    return render(request,'inout.html',{'records': records, 'fromrecords': fromrecords})
            elif "saveFromRegion" in request.POST:
                if formFromRegion.is_valid():
                    formFromRegion.save()
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
        
def updateTo(request, pk):
    if request.user.is_authenticated:
        updateIt = get_object_or_404(ToRegion, pk=pk)
        if updateIt.date_received:
            formatted_date_received = updateIt.date_received.strftime("%Y-%m-%d")
        else:
            formatted_date_received = None
        if updateIt.document_date:
            formatted_document_date = updateIt.document_date.strftime("%Y-%m-%d")
        else:
            formatted_document_date = None
        if updateIt.date_signed_sa:
            formatted_date_signed_sa = updateIt.date_signed_sa.strftime("%Y-%m-%d")
        else:
            formatted_date_signed_sa = None
        if updateIt.date_sent_out:
            formatted_date_sent_out = updateIt.date_sent_out.strftime("%Y-%m-%d")
        else:
            formatted_date_sent_out = None
        if updateIt.date_received_from_region:
            formatted_date_received_from_region = updateIt.date_received_from_region.strftime("%Y-%m-%d")
        else:
            formatted_date_received_from_region = None
        if updateIt.date_received_by_region:
            formatted_date_received_by_region = updateIt.date_received_by_region.strftime("%Y-%m-%d")
        else:
            formatted_date_received_by_region = None
        if updateIt.date_sent_to_teams:
            formatted_date_sent_to_teams = updateIt.date_sent_to_teams.strftime("%Y-%m-%d")
        else:
            formatted_date_sent_to_teams = None
        context = {'updateIt': updateIt, 
                'formatted_date_received':formatted_date_received,
                'formatted_document_date':formatted_document_date,
                'formatted_date_signed_sa':formatted_date_signed_sa,
                'formatted_date_sent_out':formatted_date_sent_out,
                    'formatted_date_received_from_region':formatted_date_received_from_region,
                    'formatted_date_received_by_region':formatted_date_received_by_region,
                    'formatted_date_sent_to_teams':formatted_date_sent_to_teams,
                }
        if request.method == 'POST':
            records = ToRegion.objects.all()
            fromrecords = FromRegion.objects.all()
            current_record = ToRegion.objects.get(id=pk)
            form =ToRegionForm(request.POST, instance=current_record)
            if form.is_valid():
                form.save()
                messages.success(request, 'Record has been updated')
                return redirect('inout')
            return render(request,'updateToRegion.html',context)
        else:
            return render(request,'updateToRegion.html',context)
    
def toDetails(request, pk):
    if request.user.is_authenticated:
        toDetails = get_object_or_404(ToRegion, pk=pk)
        context = {'toDetails': toDetails}
        return render(request,'toDetails.html', context)