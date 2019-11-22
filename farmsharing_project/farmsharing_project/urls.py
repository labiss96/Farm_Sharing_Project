from django.contrib import admin
from django.urls import path, include
import main.views
import accounts.views
import landBoard.views
import otherBoard.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('landBoard/', include('landBoard.urls')),
    path('otherBoard/', include('otherBoard.urls')),
    path('', include('main.urls')),
]
