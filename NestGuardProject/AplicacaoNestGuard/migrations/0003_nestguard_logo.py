# Generated by Django 5.0.6 on 2024-06-24 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AplicacaoNestGuard', '0002_rename_logo_nestguard_logograndeclaro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nestguard',
            name='logo',
            field=models.ImageField(default=1, upload_to='logo/'),
            preserve_default=False,
        ),
    ]
