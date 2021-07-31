# Generated by Django 3.1.6 on 2021-04-18 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisapp', '0018_auto_20210417_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardian',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='classAdmitted',
            field=models.CharField(choices=[('Basic 1', 'Basic 1'), ('Basic 2', 'Basic 2'), ('Basic 3', 'Basic 3'), ('Basic 4', 'Basic 4'), ('Basic 5', 'Basic 5'), ('Basic 6', 'Basic 6'), ('Basic 7', 'Basic 7'), ('Basic 8', 'Basic 8'), ('Basic 9', 'Basic 9')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='level',
            field=models.CharField(choices=[('Basic 1', 'Basic 1'), ('Basic 2', 'Basic 2'), ('Basic 3', 'Basic 3'), ('Basic 4', 'Basic 4'), ('Basic 5', 'Basic 5'), ('Basic 6', 'Basic 6'), ('Basic 7', 'Basic 7'), ('Basic 8', 'Basic 8'), ('Basic 9', 'Basic 9')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='payments',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='results',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]