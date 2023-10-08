from django.shortcuts import render

from config.models import AppearanceSettings

# Create your views here.

def home(request):
    apariencia = AppearanceSettings.objects.first()
    if not apariencia:
        apariencia = AppearanceSettings.objects.create()
    
    # Pasar current_section al contexto para usarlo en la plantilla
    context = {
        'apariencia': apariencia,
        # ... otros contextos si los hay ...
    }
    
    return render(request, 'base.html', context)
