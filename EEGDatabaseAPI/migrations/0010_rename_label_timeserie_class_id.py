# Generated by Django 4.2.1 on 2023-05-04 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EEGDatabaseAPI', '0009_rename_class_id_timeserie_label'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timeserie',
            old_name='label',
            new_name='class_id',
        ),
    ]