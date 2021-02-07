# Generated by Django 3.1.3 on 2020-11-12 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assembledconstruction',
            name='assemble_instruction',
            field=models.FileField(upload_to='instructions'),
        ),
        migrations.AlterField(
            model_name='assembledconstruction',
            name='image',
            field=models.ImageField(upload_to='constructionsImages'),
        ),
        migrations.AlterField(
            model_name='assembledconstruction',
            name='schema',
            field=models.ImageField(upload_to='schemas'),
        ),
        migrations.AlterField(
            model_name='component',
            name='image',
            field=models.ImageField(upload_to='componentImages'),
        ),
    ]