# forms.py
from django import forms
from .models import AppearanceSettings

class AppearanceSettingsForm(forms.ModelForm):
    menu_background_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    menu_text_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    mega_menu_background_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    mega_menu_text_color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    menu_height = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 50, 'max': 200}))
    color_principal_texto= forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))

    class Meta:
        model = AppearanceSettings
        fields = ['menu_background_color', 'menu_text_color', 'mega_menu_background_color', 'mega_menu_text_color', 'menu_height', 'color_principal_texto']
