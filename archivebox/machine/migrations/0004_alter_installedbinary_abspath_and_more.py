# Generated by Django 5.1.1 on 2024-10-03 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("machine", "0003_alter_installedbinary_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="installedbinary",
            name="abspath",
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name="installedbinary",
            name="binprovider",
            field=models.CharField(blank=True, default=None, max_length=31),
        ),
        migrations.AlterField(
            model_name="installedbinary",
            name="machine",
            field=models.ForeignKey(
                blank=True,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="machine.machine",
            ),
        ),
        migrations.AlterField(
            model_name="installedbinary",
            name="name",
            field=models.CharField(blank=True, default=None, max_length=63),
        ),
        migrations.AlterField(
            model_name="installedbinary",
            name="sha256",
            field=models.CharField(blank=True, default=None, max_length=64),
        ),
        migrations.AlterField(
            model_name="installedbinary",
            name="version",
            field=models.CharField(blank=True, default=None, max_length=32),
        ),
    ]
