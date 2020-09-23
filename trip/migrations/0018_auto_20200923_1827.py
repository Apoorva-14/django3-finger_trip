# Generated by Django 3.0.7 on 2020-09-23 18:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0017_auto_20200923_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
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
