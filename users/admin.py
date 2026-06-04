

from django.contrib import admin
from .models import UserRegister, package,LoginHistory
from .models import Booking


admin.site.register(UserRegister)
admin.site.register(LoginHistory)
admin.site.register(package)

admin.site.register(Booking)
