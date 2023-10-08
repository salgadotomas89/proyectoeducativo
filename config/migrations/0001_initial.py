# Generated by Django 4.2 on 2023-10-05 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppearanceSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_background_color', models.CharField(default='#FFFFFF', max_length=7)),
                ('menu_text_color', models.CharField(default='#000000', max_length=7)),
                ('mega_menu_background_color', models.CharField(default='#FFFFFF', max_length=7)),
                ('mega_menu_text_color', models.CharField(default='#000000', max_length=7)),
            ],
        ),
    ]