# Generated by Django 4.0 on 2023-11-05 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mob_number',
            field=models.IntegerField(),
        ),
    ]
