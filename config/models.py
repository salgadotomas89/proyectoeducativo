from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
# models.py
from django.db import models

class AppearanceSettings(models.Model):
    menu_background_color = models.CharField(max_length=7, default="#FFFFFF")
    menu_text_color = models.CharField(max_length=7, default="#000000")
    menu_height = models.PositiveIntegerField(default=80, validators=[MinValueValidator(50), MaxValueValidator(200)])

    mega_menu_background_color = models.CharField(max_length=7, default="#FFFFFF")
    mega_menu_text_color = models.CharField(max_length=7, default="#000000")

    color_principal_texto = models.CharField(max_length=7, default="#000000")

    # ... otros campos según tus necesidades ...
