# views.py
from django.shortcuts import render, redirect
from .models import AppearanceSettings
from .forms import AppearanceSettingsForm

def configuracion(request):
    apariencia = AppearanceSettings.objects.first()
    if not apariencia:
        apariencia = AppearanceSettings.objects.create()

    if request.method == 'POST':
        form = AppearanceSettingsForm(request.POST, instance=apariencia)
        if form.is_valid():
            form.save()
            # Podrías redirigir a la misma página para ver los cambios
            return redirect('home')

    else:
        form = AppearanceSettingsForm(instance=apariencia)

    current_section = request.GET.get('section', None)

    context = {
        'current_section': current_section,
        'apariencia': apariencia,
        'form': form
    }

    return render(request, 'configuracion.html', context)
