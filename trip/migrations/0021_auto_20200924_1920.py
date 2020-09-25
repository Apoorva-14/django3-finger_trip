# Generated by Django 3.0.7 on 2020-09-24 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0020_auto_20200924_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='slug',
        ),
        migrations.AlterField(
            model_name='comment',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='trip.Trip'),
        ),
        migrations.AlterField(
            model_name='like',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip.Trip'),
        ),
    ]
