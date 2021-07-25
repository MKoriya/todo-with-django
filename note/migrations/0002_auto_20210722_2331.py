# Generated by Django 3.2.5 on 2021-07-22 18:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='created_at',
        ),
        migrations.AddField(
            model_name='notes',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notes',
            name='title',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
    ]
