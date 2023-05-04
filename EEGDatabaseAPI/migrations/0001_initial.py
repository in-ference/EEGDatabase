# Generated by Django 4.2.1 on 2023-05-04 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('channel_name', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('label', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=65536)),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('type', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=65536)),
            ],
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('montage', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('createdDate', models.CharField(max_length=100)),
                ('createdBy', models.CharField(max_length=255)),
                ('protocol', models.CharField(max_length=255)),
                ('samplingRate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('samplingRateUnit', models.CharField(max_length=255)),
                ('numberOfChannels', models.IntegerField()),
                ('numberOfClasses', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_name', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=65536)),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EEGDatabaseAPI.measure')),
            ],
        ),
        migrations.CreateModel(
            name='Trial',
            fields=[
                ('trial_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('run', models.IntegerField()),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EEGDatabaseAPI.classes')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EEGDatabaseAPI.session')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSerie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.FloatField()),
                ('value', models.FloatField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EEGDatabaseAPI.channel')),
                ('trial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EEGDatabaseAPI.trial')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='measure',
            name='metadata',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EEGDatabaseAPI.metadata'),
        ),
    ]
