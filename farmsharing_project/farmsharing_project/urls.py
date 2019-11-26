from django.contrib import admin
from django.urls import path, include
import main.views
import accounts.views
import landBoard.views
import otherBoard.views
import additionBoard.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('landBoard/', include('landBoard.urls')),
    path('otherBoard/', include('otherBoard.urls')),
    path('additionBoard/', include('additionBoard.urls')),
    path('', include('main.urls')),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
