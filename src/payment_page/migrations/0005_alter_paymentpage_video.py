# -*- coding: utf-8 -*-
# Generated by Django 4.2.9 on 2024-02-06 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailvideos", "0002_alter_video_thumbnail"),
        ("payment_page", "0004_alter_paymentpage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymentpage",
            name="video",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailvideos.video",
            ),
        ),
    ]
