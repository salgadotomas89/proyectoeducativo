# Generated by Django 4.2 on 2023-10-07 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_appearancesettings_menu_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='appearancesettings',
            name='color_principal_texto',
            field=models.CharField(default='#000000', max_length=7),
        ),
    ]
