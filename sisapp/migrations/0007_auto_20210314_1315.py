# Generated by Django 3.1.6 on 2021-03-14 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisapp', '0006_auto_20210314_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='position',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
