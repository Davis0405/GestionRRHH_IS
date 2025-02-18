from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rrhh/', include('rrhh.urls')),  # URLs de tu aplicación
    path('accounts/', include('django.contrib.auth.urls')),  # URLs de autenticación
]
