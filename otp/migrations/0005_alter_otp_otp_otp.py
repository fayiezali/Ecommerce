# Generated by Django 4.1.3 on 2022-12-24 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0004_alter_otp_otp_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='otp_otp',
            field=models.CharField(default='0000', max_length=4),
        ),
    ]
