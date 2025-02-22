# Generated by Django 3.0.7 on 2020-06-21 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('rest_tournament_manager_app', '0011_tournamentmodel_tournament_max_number_of_players'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matchmodel',
            old_name='match_winner',
            new_name='match_player_a',
        ),
        migrations.RenameField(
            model_name='matchmodel',
            old_name='match_loser',
            new_name='match_player_b',
        ),
        migrations.RenameField(
            model_name='matchmodel',
            old_name='match_losing_score',
            new_name='match_score_a',
        ),
        migrations.RenameField(
            model_name='matchmodel',
            old_name='match_winning_score',
            new_name='match_score_b',
        ),
        migrations.AddField(
            model_name='matchmodel',
            name='next_match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='rest_tournament_manager_app.MatchModel'),
        ),
    ]
