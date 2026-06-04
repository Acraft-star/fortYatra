from django.contrib import admin
from django.urls import path
from fortYatra import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing),
    path('home/', views.home),
    path('fort-us/', views.fortus),
    path('books/', views.books),
    path('book-trip/', views.booking),
    path('best-packages/', views.best_packages),
    path('', include('users.urls')),
    path('packages/', views.best_packages, name='best_packages'),
    path('about/', views.about)
]
