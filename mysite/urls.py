"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("cars/",include("cars.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("signup/",views.signup,name="signup"),
    path("users/", include("users.urls")),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("profile/",views.profile_views,name="profile"),
    path("profile_edit/<int:id>/",views.profile_edit,name="profile_edit"),
    path("profile/",views.profile_views,name="profile"),
    path("address/<int:id>/",views.address,name="address"),
    path("pbuy/",views.PBuy,name="pbuy"),
    path("binfo/<int:id>/",views.BInfo,name="binfo"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="users/password_reset_form.html"), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name='password_reset_complete'),
]

urlpatterns += [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)