# Generated by Django 3.0.7 on 2020-06-20 10:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('rest_tournament_manager_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchmodel',
            name='is_finished',
        ),
        migrations.RemoveField(
            model_name='matchmodel',
            name='player_a',
        ),
        migrations.RemoveField(
            model_name='matchmodel',
            name='player_a_score',
        ),
        migrations.RemoveField(
            model_name='matchmodel',
            name='player_b',
        ),
        migrations.RemoveField(
            model_name='matchmodel',
            name='player_b_score',
        ),
        migrations.RemoveField(
            model_name='matchmodel',
            name='stage',
        ),
        migrations.RemoveField(
            model_name='matchmodel',
            name='tournament_id',
        ),
        migrations.RemoveField(
            model_name='playermodel',
            name='player_name',
        ),
        migrations.RemoveField(
            model_name='tournamentmodel',
            name='is_finished',
        ),
        migrations.RemoveField(
            model_name='tournamentmodel',
            name='number_of_stages',
        ),
        migrations.RemoveField(
            model_name='tournamentmodel',
            name='winner',
        ),
        migrations.AddField(
            model_name='matchmodel',
            name='match_loser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loser',
                                    to='rest_tournament_manager_app.PlayerModel'),
        ),
        migrations.AddField(
            model_name='matchmodel',
            name='match_losing_score',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='matchmodel',
            name='match_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='matchmodel',
            name='match_players',
            field=models.ManyToManyField(to='rest_tournament_manager_app.PlayerModel'),
        ),
        migrations.AddField(
            model_name='matchmodel',
            name='match_stage',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='matchmodel',
            name='match_tournament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tournament',
                                    to='rest_tournament_manager_app.TournamentModel'),
        ),
        migrations.AddField(
            model_name='matchmodel',
            name='match_winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner',
                                    to='rest_tournament_manager_app.PlayerModel'),
        ),
        migrations.AddField(
            model_name='matchmodel',
            name='match_winning_score',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='playermodel',
            name='player_first_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='playermodel',
            name='player_last_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='matchmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='playermodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='tournament_name',
            field=models.CharField(max_length=255),
        ),
    ]
