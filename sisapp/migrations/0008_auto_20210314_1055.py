# Generated by Django 3.1.6 on 2021-03-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisapp', '0007_auto_20210314_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=17, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='results',
            name='level',
        ),
        migrations.RemoveField(
            model_name='results',
            name='term',
        ),
    ]
