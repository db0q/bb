# Generated by Django 4.2.7 on 2023-11-15 16:57

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bedaia', '0004_remove_bedaia_discription_remove_bedaia_logo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bedaia',
            name='firstdiscription',
            field=models.TextField(default=' null '),
        ),
        migrations.AlterField(
            model_name='bedaia',
            name='firstpic',
            field=cloudinary.models.CloudinaryField(default='null ', max_length=255, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='bedaia',
            name='seconddiscription',
            field=models.TextField(default=' null '),
        ),
        migrations.AlterField(
            model_name='bedaia',
            name='secondpic',
            field=cloudinary.models.CloudinaryField(default=' null ', max_length=255, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='nukhba',
            name='firstdiscription',
            field=models.TextField(default=' null '),
        ),
        migrations.AlterField(
            model_name='nukhba',
            name='firstpic',
            field=cloudinary.models.CloudinaryField(default='null ', max_length=255, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='nukhba',
            name='seconddiscription',
            field=models.TextField(default=' null '),
        ),
        migrations.AlterField(
            model_name='nukhba',
            name='secondpic',
            field=cloudinary.models.CloudinaryField(default=' null ', max_length=255, verbose_name='Image'),
        ),
    ]