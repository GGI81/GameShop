# Generated by Django 4.0.3 on 2022-04-08 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='CurrentGame',
        ),
    ]
