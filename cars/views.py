from django.shortcuts import render, redirect
from cars.models import AddCar
from cars.forms import AddCars_Forms,Contact_Forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
    carlist = AddCar.objects.all()
    context={
        "carlist":carlist,
    }
    return render(request, "cars/home.html",context)

def about(request):
    return render(request,"cars/about.html")

def contact(request):
    forms = Contact_Forms(request.POST or None)

    if forms.is_valid():
        forms.save()
        messages.success(
            request,
            f"Dear {request.user.username}, your message is send Successfully To Emon Cars We will soon contact you...."
        )
        return redirect("cars:home")
    
    context={
        "forms":forms
    }
    
    return render(request,"cars/contact.html",context)

@login_required(login_url="login")
def Add_cars(request):
    forms = AddCars_Forms(request.POST or None,request.FILES)

    if forms.is_valid():
        forms.instance.cars_person_name = request.user.username
        forms.save()
        messages.success(
            request,
            f"Your Car {request.user.username}, is Successfully Add"
        )
        return redirect("cars:home")
    else:
        forms = AddCars_Forms(request.POST or None)

    context={
        "forms":forms
    }
    return render(request,"cars/Add_cars.html",context)

def detail(request,car_id):

    cars = AddCar.objects.get(pk = car_id)

    context ={
        "cars":cars
    }
    return render(request,"cars/detail.html",context)


def update_cars(request, id):
    addcars = AddCar.objects.get(pk=id)

    if request.method == 'POST':
        forms = AddCars_Forms(request.POST , request.FILES, instance=addcars)
        if forms.is_valid():
            forms.save()
            messages.success(
                request,
                f"Your Car {request.user.username}, is Successfully Edit "
            )
            return redirect("cars:home")
    else:
        forms = AddCars_Forms(instance=addcars)

    context = {
        "forms": forms
    }

    return render(request, "cars/update_cars.html", context)

def delete_cars(request,id):
    cars = AddCar.objects.get(pk=id)

    context={
        "cars":cars
    }

    if request.method == "POST":
        cars.delete()
        messages.success(
            request,
            f"Your Car {request.user.username}, is Successfully delete "
        )
        return redirect("cars:home")
    
    return render(request,"cars/delete_cars.html",context)


def searchbar(request):
    if request.method == "GET":
        searchfor= request.GET.get("search")
        search = AddCar.objects.filter(cars_name__icontains=searchfor)
        
        context = {
           "search":search,
           "searchfor": searchfor,
           "no_results" : not search.exists(),
        }
       
    return render(request,"cars/searchbar.html",context)




