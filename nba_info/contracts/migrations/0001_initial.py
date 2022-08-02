# Generated by Django 4.0.6 on 2022-08-02 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
        ('players', '0002_alter_player_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='players.player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='teams.team')),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('year', models.IntegerField()),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salaries', to='contracts.contract')),
            ],
        ),
    ]