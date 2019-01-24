from django.contrib import admin
from myapp.models import User
from myapp.models import educators,file
admin.site.register(User)
admin.site.register(educators)
admin.site.register(file)


