# Generated by Django 4.0.3 on 2022-04-07 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0010_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='no_profile.jpg', null=True, upload_to=''),
        ),
    ]
