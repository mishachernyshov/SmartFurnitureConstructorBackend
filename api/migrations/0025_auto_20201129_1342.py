# Generated by Django 3.1.3 on 2020-11-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_assembledconstruction_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='weight',
            field=models.FloatField(),
        ),
    ]