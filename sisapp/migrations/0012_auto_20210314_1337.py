# Generated by Django 3.1.6 on 2021-03-14 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sisapp', '0011_auto_20210314_1326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='results',
            options={'ordering': ['-level'], 'verbose_name_plural': 'Results'},
        ),
    ]
