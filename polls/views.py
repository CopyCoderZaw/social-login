from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

### all page middleware
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *

### for weather
import requests
import json
# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        userinput = request.POST['username']
        try:
            username =  CustomUser.objects.get(email=userinput).username
        except CustomUser.DoesNotExist:
            username = request.POST['username']
        
        password = request.POST['password']

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('indexpage')
        else:
            messages.error(request, 'Username or password is incorrect!')


        
    return render(request, 'pages/samples/login.html')

def logoutPage(request):
    logout(request)
    return redirect('loginpage')

#### register
def registerpage(request):
    form = MyCustomForm()
    if request.method == 'POST':
        form = MyCustomForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.save()

            user = authenticate(request, username=user.username, password1 = request.POST['password1'],password2 = request.POST['password2'])

            if user is not None:
                login(request, user)
        return redirect('loginpage')
    context = {'form':form}
    
    return render(request, 'pages/samples/register.html',context)

### profile page
@login_required(login_url='loginpage')
def profile(request):
    page = 'pro'
    return render(request, 'pages/samples/profile.html',{'page':page})

##### profile change
@login_required(login_url='loginpage')
def changeprof(request):
    page = 'changeprofile'

    user = request.user
    form = ProForm(instance=user)

    if request.method == 'POST':
        form = ProForm(request.POST,  request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('profilepage')
    context = {"page":page,'form':form}
    return render(request, 'pages/samples/profile.html',context)

##### change password
@login_required(login_url='loginpage')
def changepass(request):
    context = {}
    if request.method == 'POST':
        current = request.POST['cpwd']
        new_pass = request.POST['npwd']

        user = CustomUser.objects.get(id=request.user.id)
        check = user.check_password(current)

        if check==True:
            user.set_password(new_pass)
            user.save()
            context["msz"] = "Password Changee Successfully !!!"
            context["col"] = "alert-success"
        else:
            context["msz"] = "Incorrect Current Password"
            context["col"] = "alert-danger"

    return render(request, 'pages/samples/changepass.html',context)

#### homepage
@login_required(login_url='loginpage')
def home(request):
    
    
    return render(request, 'pages/index.html')

###### table
def table(request):
    return render(request, 'pages/tables/tables.html')

#### all show
def all_show(request):
    return render(request, 'pages/tables/sh-table.html')

#### table per_views
def per_views(request):
    return render(request, 'pages/tables/per_views.html')

#### table create
def create(request):
    return render(request, 'pages/tables/cretab.html')

def basic(request):
    return render(request, 'pages/forms/basic_elements.html')

###################### photo start #####################
#### arakan photo
def army_pho(request):
    year = request.GET.get('year')
    
    if year == None:
        photos = Photo.objects.all().order_by('-id')
    else:
        photos = Photo.objects.filter(year__name=year)
        
    years = Year.objects.all()
    context = {
        "years":years,
        'photos':photos
    }
    return render(request, 'pages/arakan photo/armypho.html',context)

#### create photo
def crephoto(request):
    page = 'create'
    years = Year.objects.all()
        #### multiple image
    if request.method == "POST":
        data = request.POST
        images = request.FILES.getlist('images')

        if data['year'] :
            year = Year.objects.get(id = data['year'])

        for image in images:
           photo = Photo.objects.create(
               year = year,
               title = data['title'],
               image = image,
           )

        return redirect('armyphotopage')
             
    context = {
        "page":page,
        'years':years
    }
    return render(request, 'pages/arakan photo/crephoto.html',context)

### edit photo
def edit_photo(request):
    page = 'edit'
    context ={
        'page':page
    }
    return render(request, 'pages/arakan photo/crephoto.html',context)

###### view photo
def photo_view(request,pk):
    years = Year.objects.all()
    photos = Photo.objects.get(id=pk)
    return render(request, 'pages/arakan photo/view.html',{'years':years,'photos':photos})

################# year start #####################

#### create year
def crtyear(request):
    page = 'create'
    years = Year.objects.all()
    
    ### create page
    form = YearForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        form = YearForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"{} Creating successfully alert !!!".format(name))
            return redirect('crtyearpage')
        
    context = {
        'page':page,
        "years":years,
        "form":form,
    }

    return render(request,'pages/arakan photo/cteyear.html',context)

### edit year
def edityear(request,pk):
    page = 'edit'
    years = Year.objects.all()
    year = Year.objects.get(id=pk)
    form = YearForm(instance=year)
    if request.method == "POST":
        name = request.POST.get('name')
        form = YearForm(request.POST,instance=year)
        if form.is_valid():
            form.save()
            messages.success(request,"{} Editing successfully alert !!!".format(name))
            return redirect('crtyearpage')
    
    context = {
        "page":page,
        'years':years,
        'year':year
    }
    return render(request, 'pages/arakan photo/cteyear.html',context)

## delete year
def delyear(request, pk):
    year = Year.objects.get(id=pk)
    year.delete()
    messages.success(request, "Your Delete Success!!!")
    return redirect('crtyearpage')

############################  another #####################################

