# Generated by Django 4.1.3 on 2023-01-11 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatsapp', '0009_alter_sendotptowhatsappmodel_is_whatsapp_active'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
