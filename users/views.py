from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.hashers import make_password, check_password
from io import BytesIO
from xhtml2pdf import pisa
from .models import UserRegister, LoginHistory
import random

from .models import UserRegister, package, Booking


from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def register(request):
    if request.method == "POST":

        full_name = request.POST.get("full_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        otp = random.randint(1000, 9999)

        request.session['otp'] = otp
        request.session['full_name'] = full_name
        request.session['address'] = address
        request.session['email'] = email
        request.session['phone'] = phone
        request.session['password'] = password

        try:
            send_mail(
                "FortYatra Email Verification",
                f"Your OTP is {otp}",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )

        except Exception:
            return render(request, "register.html", {
                "error": "Please enter a valid email"
            })

        return redirect("verify")

    return render(request, "register.html")


def verify(request):
    if request.method == "POST":

        entered_otp = request.POST.get("otp")

        # OTP number 
        if not entered_otp.isdigit():
            return render(request, "verify.html", {
                "error": "OTP must contain only numbers"
            })

        if int(entered_otp) == request.session['otp']:

            UserRegister.objects.create(
                full_name=request.session['full_name'],
                address=request.session['address'],
                email=request.session['email'],
                phone=request.session['phone'],
                password=make_password(request.session['password'])
            )

            return redirect("login")

        else:
            return render(request, "verify.html", {
                "error": "Wrong OTP"
            })

    return render(request, "verify.html")


def thank_you(request):
    return render(request, "thank_you.html", {"full_name": "Guest"})


def booking(request, id):
    pkg = package.objects.get(id=id)

    seats_left = pkg.seats

    if seats_left <= 0:
        return render(request, "sold_out.html")

    if request.method == "POST":

        your_name = request.POST.get("name")
        your_address = request.POST.get("address")
        your_contact = request.POST.get("your_contact")
        your_email = request.POST.get("email")
        driver_name = request.POST.get("driver")
        trip_date = request.POST.get("date")
        contact = request.POST.get("contact")
        package_name = request.POST.get("package")

        seat = int(request.POST.get("seat"))
        total_price = int(request.POST.get("total_price"))
        payment_method = request.POST.get("payment_method", "Cash")

        if seat > pkg.seats:
            return render(request, "booking.html", {
                "pkg": pkg,
                "error": "Not enough seats available!"
            })

        booking_obj = Booking.objects.create(
            package=pkg,
            your_name=your_name,
            your_address=your_address,
            your_contact=your_contact,
            your_email=your_email,
            driver_name=driver_name,
            trip_date=trip_date,
            contact=contact,
            package_name=package_name,
            seats_booked=seat,
            total_price=total_price,
            payment_method=payment_method
        )

        pkg.seats -= seat
        pkg.save()

        template_path = 'booking_pdf.html'
        context = {
            'your_name': your_name,
            'driver_name': driver_name,
            'driver_contact': contact,
            'package_name': package_name,
            'seat': seat,
            'total_price': total_price,
            'payment_method': payment_method,
            'trip_date': trip_date,
        }

        html = render_to_string(template_path, context)

        pdf_file = BytesIO()
        pisa.CreatePDF(html, dest=pdf_file)
        pdf_file.seek(0)

        email = EmailMessage(
            subject="Confirm your Booking",
            body=f"Thank you {your_name} for travelling on FortYatra Website!",
            from_email='FortYatra <noreply@fortyatra.com>',
            to=[your_email],
            reply_to=[settings.EMAIL_HOST_USER],
        )

        email.attach(
            f"Booking_{your_name}.pdf",
            pdf_file.read(),
            'application/pdf'
        )
        email.send(fail_silently=False)

        return render(request, "boking_conf.html", {"your_name": your_name})

    return render(request, 'booking.html', {"pkg": pkg})


def booking_conf(request):
    return render(request, "booking_conf.html", {"your_name": "Guest"})

from .models import UserRegister, LoginHistory
def login(request):
    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        # latest user record fetch
        user = UserRegister.objects.filter(email=email).order_by('-id').first()

        # email not found
        if user is None:
            return render(request, "login.html", {
                "error": "Email Not Registered"
            })

        # password check
        if check_password(password, user.password):

            # save login history
            LoginHistory.objects.create(
                user=user,
                email=user.email
            )

            # session start
            request.session['user_name'] = user.full_name
            request.session['user_email'] = user.email
            request.session['user_id'] = user.id

            return redirect("home")

        else:
            return render(request, "login.html", {
                "error": "Your Password is Wrong"
            })

    return render(request, "login.html")


def home(request):
    return render(request, "landing.html")


def logout(request):
    request.session.flush()
    return redirect("home")


def my_booking(request):
    email = request.session.get('user_email')
    bookings = Booking.objects.filter(your_email=email)

    return render(request, "my_booking.html", {"bookings": bookings})


def create_package(request):
    if request.method == "POST":

        package.objects.create(
            fort_name=request.POST.get("fort_name"),
            driver_name=request.POST.get("driver_name"),
            contact=request.POST.get("contact"),
            pickup_place=request.POST.get("pickup_place"),
            pickup_date=request.POST.get("pickup_date"),
            seats=request.POST.get("seats"),
            price=request.POST.get("price"),
            offer_price=request.POST.get("offer_price"),
            created_by_user=True
        )

        return redirect('best_packages')

    return render(request, 'create_package.html')






def about(request):
    return render(request, "about.html")





