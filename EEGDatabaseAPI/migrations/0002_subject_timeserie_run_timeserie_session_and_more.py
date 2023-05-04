# Generated by Django 4.2.1 on 2023-05-04 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EEGDatabaseAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=65536)),
            ],
        ),
        migrations.AddField(
            model_name='timeserie',
            name='run',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='timeserie',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EEGDatabaseAPI.session'),
        ),
        migrations.AlterField(
            model_name='measure',
            name='description',
            field=models.CharField(blank=True, max_length=65536, null=True),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='numberOfChannels',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='numberOfClasses',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='description',
            field=models.CharField(blank=True, max_length=65536, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_name',
            field=models.CharField(default='Training', max_length=255, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='timeserie',
            name='trial',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Trial',
        ),
        migrations.AddField(
            model_name='timeserie',
            name='subject_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EEGDatabaseAPI.subject'),
        ),
    ]
