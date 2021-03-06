# Generated by Django 3.1.6 on 2021-03-14 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=255, null=True, unique=True, verbose_name='username')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('firstname', models.CharField(max_length=255, null=True, verbose_name='firstname')),
                ('lastname', models.CharField(max_length=255, null=True, verbose_name='lastname')),
                ('othername', models.CharField(blank=True, max_length=255, null=True, verbose_name='othernames')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='null', max_length=255, null=True, verbose_name='gender')),
                ('date_of_birth', models.DateField(auto_now_add=True)),
                ('group', models.CharField(default='null', max_length=2, null=True)),
                ('level', models.CharField(default='null', max_length=10, null=True)),
                ('yearOfadmission', models.CharField(default='null', max_length=10, null=True)),
                ('classAdmitted', models.CharField(default='null', max_length=10, null=True)),
                ('is_student', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('othername', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('profession', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('gps', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=30)),
                ('amount', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('title', models.CharField(max_length=20)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='guardian',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sisapp.guardian'),
        ),
    ]
