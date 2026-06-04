from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from users.models import package


def landing(request):
    return render(request, "landing.html")

def home(request):
    return render(request, "home.html")

def fortus(request):
    return render(request, "fort.html")

def books(request):
    return render(request, "books.html")

def about(request):
     return render(request, "about.html")

def booking(request):         
    n1 = str(request.POST.get('name'))
    n2 = request.POST.get('mobile')
    n3 = str(request.POST.get('fort_name'))
    n4 = request.POST.get('trip_date')
    n5 = request.POST.get('persons')
    
    
    print(n1,n2,n3,n4,n5)
    return render(request, "trip.html")

def best_packages(request):
    packagesData = package.objects.all()   # () important

    data = {
        'packagesData': packagesData
    }

    return render(request, 'package.html', data)



