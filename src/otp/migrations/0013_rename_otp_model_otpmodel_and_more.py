# Generated by Django 4.1.3 on 2023-01-05 14:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('otp', '0012_rename_phonemodel_phone_modell'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='otp_MODEL',
            new_name='otpMODEL',
        ),
        migrations.RenameModel(
            old_name='Phone_MODELl',
            new_name='PhoneMODELl',
        ),
    ]
