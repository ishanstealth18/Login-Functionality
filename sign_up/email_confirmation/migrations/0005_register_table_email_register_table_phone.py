# Generated by Django 4.2.6 on 2023-12-23 13:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('email_confirmation', '0004_alter_register_table_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_table',
            name='email',
            field=models.EmailField(default=0, max_length=155),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register_table',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
