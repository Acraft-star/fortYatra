from django.shortcuts import render
from .models import UserRegister 
from django.core.mail import send_mail
from django.conf import settings

def register(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        # Save to DB
        UserRegister.objects.create(
            full_name=full_name,
            address=address,
            email=email,
            phone=phone
        )

        # Send Email
        send_mail(
            "Registration Successful",
            f"Thank you {full_name} for registering on FortYatra Website!",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        # Render Thank You page with user name
        return render(request, "thank_you.html", {"full_name": full_name})

    return render(request, "register.html")


def thank_you(request):
    # Optional fallback if someone visits /thank-you directly
    return render(request, "thank_you.html", {"full_name": "Guest"})