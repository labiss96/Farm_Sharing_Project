from django.contrib import admin
from .models import SharingBoard
from .models import Region
from .models import RequestBoard

admin.site.register(SharingBoard)
admin.site.register(Region)
admin.site.register(RequestBoard)
