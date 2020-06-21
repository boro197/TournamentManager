# Generated by Django 3.0.7 on 2020-06-21 14:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('rest_tournament_manager_app', '0012_auto_20200621_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchmodel',
            name='match_tournament',
        ),
        migrations.AddField(
            model_name='tournamentmodel',
            name='tournament_matches',
            field=models.ManyToManyField(to='rest_tournament_manager_app.MatchModel'),
        ),
    ]
