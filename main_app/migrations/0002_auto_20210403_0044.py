# Generated by Django 3.1.4 on 2021-04-03 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='elevation',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='map',
            name='name',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='map',
            name='region',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='map',
            name='subregion',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
    ]