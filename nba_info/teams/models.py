from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def top_players_by_salary(self):
        """Return a list of players sorted by their maximum salary."""
        return self.players\
            .annotate(max_salary=models.Max('contract__salaries__salary'))\
            .order_by('-max_salary')
