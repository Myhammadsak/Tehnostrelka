# Generated by Django 5.1.6 on 2025-03-09 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_generes'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]
