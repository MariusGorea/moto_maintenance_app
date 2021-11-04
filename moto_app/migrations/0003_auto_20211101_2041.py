# Generated by Django 3.2.8 on 2021-11-01 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moto_app', '0002_auto_20211101_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldpart',
            name='part',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='moto_app.part'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='soldpart',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
