from django.contrib import admin
from home.models import Contact
from home.models import Login
from home.models import Signup

# Register your models here.
admin.site.register(Contact)
admin.site.register(Login)
admin.site.register(Signup)