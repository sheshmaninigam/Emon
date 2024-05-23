from users import views
from django.urls import path

app_name = "users"

urlpatterns = [
     # paypal checkout button
     path("buy/<int:id>/",views.Payment, name="buy"),

     # paypal on approve
     path("oa/",views.OnApprove,name="oa"),

     # paypal payment success
     path("ps/",views.PaymentSuccess,name="ps")
]