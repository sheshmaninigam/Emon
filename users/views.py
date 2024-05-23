from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import SignUpForms,ProfileForm
from users.models import Profile,Address,transaction
from cars.models import AddCar
from django.urls import reverse_lazy
from users.forms import ProfileForm,AddressForm,TranscationForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.http import JsonResponse
from datetime import datetime
import uuid
import json
# Create your views here.

def signup(request):
  try:
    if request.method =="POST":
      form = SignUpForms(request.POST)

      if form.is_valid():
        username = form.cleaned_data.get("username")
        messages.success(
          request,
          f"welcome {username}, you have been Successfully Signup"
        )
        form.save()
        return redirect ("login")
      
    else:
        form = SignUpForms()
        context ={
          "form": form
        }
        
        return render(request, "users/signup.html",context)
    return HttpResponse(render(request,"users/signup.html",messages.success( request, "Invalid password, try again"),context))
   
  except UnboundLocalError:
     return render(request, "users/signup.html",{"form":form})

def login_view(request):
    
    if request.method == 'POST':
       username = request.POST["username"]
       password = request.POST["password"]
       user = authenticate(request, username=username, password=password)
       
       if user is None:
        messages.success(
           request,
           "Invalid login"
        )
        return redirect("login")

       elif user.is_superuser:
        login(request,user)
        messages.success(
            request,
            f"Welcome Superuser {request.user.username},you have been Successfully login"
        )
        return redirect("cars:home")

       elif user is not None:
        login(request,user)
        messages.success(
            request,
            f"Welcome {request.user.username},you have been Successfully login"
        )
        return redirect("cars:home")

    return render(request, "users/login.html")

def logout_view(request):
   messages.success(
      request,
      f"{request.user.username}, you have been Successfully logout"
   )
   logout(request)
   return redirect("cars:home")
  
@login_required(login_url="login")
def profile_views(request):
   return render(request, "users/profile.html")

@login_required(login_url="login")
def profile_edit(request,id):
  profile=Profile.objects.get(pk=id)
  form = ProfileForm(request.POST or None, request.FILES, instance=profile)
  if form.is_valid():
    form.save()
    messages.success(
      request,
      f"Your profile {request.user.username}, is Successfully Change"
    )
    return redirect("cars:home")
  
  else:
        form = ProfileForm(instance=profile)
  
  context = {
    "form":form
  }
   
  return render(request, "users/profile_edit.html",context)

@login_required(login_url="login")
def address(request, id):
    try:
        cars = AddCar.objects.get(pk=id)
    except AddCar.DoesNotExist:
        return render(request, 'error.html', {'error_message': 'Car not found'})
    
    forms = AddressForm(request.POST or None)

    if forms.is_valid():
        address_instance = forms.save(commit=False)
        address_instance.name = request.user.username
        address_instance.no = cars.id
        address_instance.save()
        return redirect("users:buy", cars.id)


    context = {
        "forms": forms,
        "cars": cars
    }

    return render(request, "users/address.html", context)

@login_required(login_url="login")
def Payment(request, id):
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%d-%m-%Y %I:%M:%S %p")
    print(formatted_datetime)
    cars = AddCar.objects.filter(pk=id)

    username = request.user.username
    print(username)
    
    for i in cars:
        price = i.cars_price
        band = i.cars_name
        model = i.cars_model
        name = i.cars_person_name
        image = i.cars_image
        desc = i.cars_desc
        prices = i.id
        print(price, prices,band,model,name,image,desc)
        
        request.session["price"] = price
        request.session["band"] = band
        request.session["model"] = model
        request.session["name"] = name
        request.session["prices"] = prices
        request.session["formatted_datetime"] = formatted_datetime
        
    context = {
        "cars": cars,
        "price": price,
        "prices":prices,
        "band":band,
        "model":model,
        "name":name,
        "image":image,
        "desc":desc,
        "formatted_datetime": formatted_datetime,
        "username":username
    }
   
    return render(request, "users/payment.html", context)

@login_required(login_url="login")
def OnApprove(request):
  
    if request.method =="POST":
        body = json.loads(request.body)
        status = body.get("status",None)
        orderid = body.get("orderID",None)
        transid = body.get("transID",None)

        print(f"Status:- {status},  OrderId:- {orderid},  TransactionId:- {transid}")

        request.session["status"] = status
        request.session["orderid"] = orderid
        request.session["transid"] = transid

        price = request.session.get("price", None)
        band = request.session.get("band", None)
        model = request.session.get("model", None)
        prices = request.session.get("prices", None)
        datetime = request.session.get("formatted_datetime", None)
    
    email = request.user.email
    print(email)

    add =Address.objects.all()

    for i in add:
       if prices==i.no:
          id = i.no
          names = i.name
          address = i.address
          city = i.city
          state = i.state
          postal_code = i.postal_code
          print(id,names,address,city,state,postal_code)

    
    uuid_str = str(uuid.uuid4().int)
    unique_id = int(uuid_str[:10])
    print(unique_id)

    transact = transaction.objects.create(
       user = request.user,
       trans = transid,
       order = unique_id,
       statuses = status,
       date_time = datetime,
       brand = band,
       model = model,
       price = price,
       email=email,
       name= names,
       address = address,
       city=city,
       state=state,
       postal_code=postal_code
       


    )
    request.session["unique_id"]=unique_id


    context = {
       "status":status,
       "order":orderid,
       "transid":transid,
       "unique_id":unique_id
    }
    
    return JsonResponse(context)

    

@login_required(login_url="login")
def PaymentSuccess(request):
    price = request.session.get("price", None)
    band = request.session.get("band", None)
    model = request.session.get("model", None)
    name = request.session.get("name", None)
    status = request.session.get("status", None)
    orderid  = request.session.get("orderid", None)
    transid = request.session.get("transid", None)
    prices = request.session.get("prices", None)
    datetime = request.session.get("formatted_datetime", None)
    unique_id = request.session.get( "unique_id",None)

    print(unique_id)

    email = request.user.email
    print(email)

    add =Address.objects.all()

    for i in add:
       if prices==i.no:
          id = i.no
          names = i.name
          address = i.address
          city = i.city
          state = i.state
          postal_code = i.postal_code
          print(id,names,address,city,state,postal_code)


    
    
    context = {
        "price": price,
        "band":band,
        "model":model,
        "name":name,
        "status":status,
        "orderid":orderid,
        "transid":transid,
        "datetime":datetime,
        "names":names,
        "address":address,
        "city":city,
        "state":state,
        "postal_code":postal_code,
        "email":email,
        "unique_id":unique_id
    }

    return render(request, "users/pymtsuccess.html", context)

def PBuy(request):
    trans = transaction.objects.all()
    profile = Profile.objects.all()

    for i in trans:
       brand = i.brand
       name = i.name
       

    for i in profile:
       if i.user_type == request.user.profile.user_type:
          user_type = i.user_type
          print(user_type)

    context = {
       "trans":trans,
       "user_type":user_type,
       "brand":brand,
       "name":name

    }

    return render(request,"users/pbuy.html",context)

def BInfo(request,id):
    trans = transaction.objects.filter(pk=id)
    context = {
       "trans":trans
    }

    return render(request,"users/binfo.html",context)