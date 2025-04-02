# Generated by Django 5.2 on 2025-04-02 21:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
            preserve_default=False,
        ),
    ]
