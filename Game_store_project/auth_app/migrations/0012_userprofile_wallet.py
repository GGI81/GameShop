# Generated by Django 4.0.3 on 2022-04-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0011_alter_userprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='wallet',
            field=models.FloatField(default=0),
        ),
    ]