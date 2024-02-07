from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([PRODUCTION,Producer,Task,Supervisor,CgArtist])