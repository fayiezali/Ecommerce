# Generated by Django 4.1.3 on 2023-02-17 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0014_delete_phonemodell'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='otpmodel',
            options={'ordering': ['otp_created_at'], 'verbose_name_plural': 'OTP User Login'},
        ),
    ]
