# Generated by Django 4.1.3 on 2022-12-24 06:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('otp', '0005_alter_otp_otp_otp'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='otp',
            new_name='otp_MODEL',
        ),
        migrations.AlterModelOptions(
            name='otp_model',
            options={'ordering': ['otp_created_at']},
        ),
    ]
