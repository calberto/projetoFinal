from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.shortcuts import redirect

import core.urls


# from django.urls import path

urlpatterns = [
<<<<<<< HEAD
	path('' , include('website.urls')),
   	path('admin/', admin.site.urls),
	path('sistema/', include(core.urls)),
	path('accounts/', include('django.contrib.auth.urls')),
=======
    path('core/', include('core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
    
>>>>>>> 8aaa8fa7274a57f1c5dd7c0e8ddcdfdc4e12fc57
]

