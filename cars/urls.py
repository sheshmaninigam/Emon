from django.contrib import admin
from django.urls import path,include
from cars import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'cars'
urlpatterns = [
    path("home/",views.home,name="home"),
    path("Add_cars/",views.Add_cars,name="Add_cars"),
    path("detail/<int:car_id>/",views.detail,name="detail"),
    path("searchbar/",views.searchbar,name="searchbar"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("update_cars/<int:id>/",views.update_cars,name="update_cars"),
    path("delete_cars/<int:id>/",views.delete_cars,name="delete_cars"),
]
urlpatterns += [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)