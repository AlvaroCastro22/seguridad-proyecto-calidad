from django.contrib import admin
from .models import User, Application, UserApplicationAccess

admin.site.register(User)
admin.site.register(Application)
admin.site.register(UserApplicationAccess)