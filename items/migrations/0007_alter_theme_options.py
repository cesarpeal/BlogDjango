# Generated by Django 4.1.7 on 2023-04-01 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_theme_alter_file_filename_alter_image_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='theme',
            options={'verbose_name': 'Tema', 'verbose_name_plural': 'Temas'},
        ),
    ]
