# Generated by Django 3.0.7 on 2020-06-20 10:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('rest_tournament_manager_app', '0003_auto_20200620_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentmodel',
            name='id',
            field=models.AutoField(db_index=True, primary_key=True, serialize=False),
        ),
    ]
