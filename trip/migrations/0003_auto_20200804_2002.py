# Generated by Django 3.0.7 on 2020-08-04 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0002_auto_20200804_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]