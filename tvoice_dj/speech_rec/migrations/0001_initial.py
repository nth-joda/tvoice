# Generated by Django 4.1.5 on 2023-01-14 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpeechFileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('extensions', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('size', models.IntegerField()),
                ('path', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='speech_files')),
                ('result', models.TextField()),
            ],
        ),
    ]
