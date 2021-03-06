# Generated by Django 3.1.6 on 2021-03-14 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisapp', '0014_auto_20210314_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='guardian',
            name='fullname',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='guardian',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='classAdmitted',
            field=models.CharField(choices=[('Primary 1', 'Primary 1'), ('Primary 2', 'Primary 2'), ('Primary 3', 'Primary 3'), ('Primary 4', 'Primary 4'), ('Primary 5', 'Primary 5'), ('Primary 6', 'Primary 6'), ('JHS 1', 'JHS 1'), ('JHS 2', 'JHS 2'), ('JHS 3', 'JHS 3')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='group',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='level',
            field=models.CharField(choices=[('Primary 1', 'Primary 1'), ('Primary 2', 'Primary 2'), ('Primary 3', 'Primary 3'), ('Primary 4', 'Primary 4'), ('Primary 5', 'Primary 5'), ('Primary 6', 'Primary 6'), ('JHS 1', 'JHS 1'), ('JHS 2', 'JHS 2'), ('JHS 3', 'JHS 3')], max_length=10, null=True),
        ),
    ]
