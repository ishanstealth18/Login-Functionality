# Generated by Django 4.2.6 on 2023-12-23 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_confirmation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_table',
            name='phone',
            field=models.IntegerField(),
        ),
    ]