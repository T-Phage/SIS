# Generated by Django 3.1.6 on 2021-03-14 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisapp', '0009_auto_20210314_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='level',
            field=models.CharField(choices=[('Primary 1 Term 1', 'Primary 1 Term 1'), ('Primary 1 Term 2', 'Primary 1 Term 2'), ('Primary 1 Term 3', 'Primary 1 Term 3'), ('Primary 2 Term 1', 'Primary 2 Term 1'), ('Primary 2 Term 2', 'Primary 2 Term 2'), ('Primary 2 Term 3', 'Primary 2 Term 3'), ('Primary 3 Term 1', 'Primary 3 Term 1'), ('Primary 3 Term 2', 'Primary 3 Term 2'), ('Primary 3 Term 3', 'Primary 3 Term 3'), ('Primary 4 Term 1', 'Primary 4 Term 1'), ('Primary 4 Term 2', 'Primary 4 Term 2'), ('Primary 4 Term 3', 'Primary 4 Term 3'), ('Primary 5 Term 1', 'Primary 5 Term 1'), ('Primary 5 Term 2', 'Primary 5 Term 2'), ('Primary 5 Term 3', 'Primary 5 Term 3'), ('Primary 6 Term 1', 'Primary 6 Term 1'), ('Primary 6 Term 2', 'Primary 6 Term 2'), ('Primary 6 Term 3', 'Primary 6 Term 3'), ('JHS 1 Term 1', 'JHS 1 Term 1'), ('JHS 1 Term 2', 'JHS 1 Term 2'), ('JHS 1 Term 3', 'JHS 1 Term 3'), ('JHS 2 Term 1', 'JHS 2 Term 1'), ('JHS 2 Term 2', 'JHS 2 Term 2'), ('JHS 2 Term 3', 'JHS 2 Term 3'), ('JHS 3 Term 1', 'JHS 3 Term 1'), ('JHS 3 Term 2', 'JHS 3 Term 2'), ('JHS 3 Term 3', 'JHS 3 Term 2')], max_length=17, null=True),
        ),
        migrations.DeleteModel(
            name='Level',
        ),
    ]
