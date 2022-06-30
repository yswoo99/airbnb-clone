# Generated by Django 2.2.5 on 2022-06-30 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20220630_1825'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='check_in',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='review',
            name='cleanliness',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='review',
            name='location',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='review',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.Room'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='value',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='accuracy',
            field=models.IntegerField(default=5),
        ),
    ]
