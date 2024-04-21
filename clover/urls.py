from django.contrib import admin
from django.urls import include, path 
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='cadastro', permanent=False)),
    path('usuarios/', include('usuarios.urls')),
    path('medicos/', include('medico.urls')),
    path('pacientes/', include('paciente.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
