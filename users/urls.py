from django.urls import path
from . import views

urlpatterns = [

path("register/", views.register, name="register"),
path('thank-you/', views.thank_you, name='thank_you'),
path('booking/<int:id>/', views.booking, name='booking'),
path('booking-conf/' , views.booking_conf, name='booking_conf'),

path("", views.home, name="home"),
path("login/", views.login, name="login"),
path("logout/", views.logout, name="logout"),

path("my-booking/", views.my_booking, name="my_booking"),
path('create-package/', views.create_package, name='create_package'),
path("verify/", views.verify, name="verify"),

path("about/", views.about, name="about"),


  


]