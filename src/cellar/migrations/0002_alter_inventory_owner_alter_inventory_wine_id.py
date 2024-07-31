# Generated by Django 5.0.7 on 2024-07-31 14:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cellar', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='wine_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cellar.wines'),
        ),
    ]
