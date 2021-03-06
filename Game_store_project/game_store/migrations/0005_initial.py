# Generated by Django 4.0.3 on 2022-04-13 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game_store', '0004_delete_games'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField()),
            ],
        ),
    ]
