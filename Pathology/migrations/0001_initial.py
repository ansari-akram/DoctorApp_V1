# Generated by Django 3.0 on 2019-12-16 11:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AI_Usecase_Occurences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 16, 17, 9, 39, 765069))),
                ('Image_Output_1', models.FileField(default='', upload_to='')),
                ('confidence', models.CharField(default='', max_length=5)),
                ('heatmap', models.FileField(default='', upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image_Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image_Upload', models.FileField(upload_to='Patient_reports/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lab_Api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, unique=True)),
                ('Age', models.PositiveIntegerField()),
                ('Gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=120)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 16, 17, 9, 39, 764071))),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test_Pathology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('some_test', models.CharField(max_length=500)),
                ('api_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Scripts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_url', models.URLField(default='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('image_output', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pathology.AI_Usecase_Occurences')),
                ('location', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Pathology.Location')),
                ('patient_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pathology.Patient_Details')),
                ('test', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Pathology.Test_Pathology')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lab_Api_Scripts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_api_scripts_name', models.CharField(max_length=100)),
                ('lab_api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pathology.Lab_Api')),
                ('scripts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pathology.Scripts')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lab_Api_On_Image_Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_api_on_image_input_name', models.CharField(max_length=100)),
                ('image_input', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pathology.Image_Input')),
                ('lab_api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pathology.Lab_Api')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lab_api',
            name='test',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Pathology.Test_Pathology'),
        ),
        migrations.AddField(
            model_name='lab_api',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
