# Generated by Django 4.1.7 on 2023-04-22 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_commentary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentary',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='commentary',
            old_name='user_id',
            new_name='user',
        ),
    ]
