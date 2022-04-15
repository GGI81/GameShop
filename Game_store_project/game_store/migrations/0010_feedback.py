# Generated by Django 4.0.3 on 2022-04-15 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_store', '0009_delete_ownedgames'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(choices=[('Nice', 'Nice'), ('Maybe', 'Maybe'), ('Bad', 'Bad')], max_length=20)),
                ('feedback', models.TextField()),
            ],
        ),
    ]