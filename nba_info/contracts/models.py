from django.db import models
from nba_info.players.models import Player
from nba_info.teams.models import Team


class Contract(models.Model):
    """A potentially multi-year contract for a player.
    This currently treats short-term contracts as one year."""
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(
        Team,
        related_name='contracts',
        on_delete=models.CASCADE
    )
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return f'{self.team} - {self.player}'


class Salary(models.Model):
    """Salary for ONE year of a contract."""
    contract = models.ForeignKey(
        Contract,
        related_name='salaries',
        on_delete=models.CASCADE
    )
    salary = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return f'{self.contract} - {self.year} - {self.salary}'

    class Meta:
        verbose_name_plural = 'salaries'
