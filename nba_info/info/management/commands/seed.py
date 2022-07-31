import sys

import requests
from django.core.management.base import BaseCommand
from nba_info.players.models import Player
from nba_info.teams.models import Team


class Command(BaseCommand):
    help = 'seed database'

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed()
        self.stdout.write('done.')


def run_seed():
    API_BASE = 'https://www.balldontlie.io/api/v1'

    try:
        r = requests.get(f'{API_BASE}/teams')
        r.raise_for_status()
    except requests.RequestException as req_exception:
        print(f'Error: {req_exception}')
        sys.exit(1)

    try:
        teams = r.json()['data']
        for team in teams:
            Team.objects.create(
                id=team['id'],
                name=team['full_name'],
            )
    except KeyError as key_error:
        print(f'Error: {key_error}')
        sys.exit(1)

    print('Seeded teams.')

    page = 0

    # Pages start at 1 and end at meta['total_pages'] (not 0-indexed).
    while True:
        page += 1
        print('Fetching player page', page)
        try:
            r = requests.get(f'{API_BASE}/players?page={page}&per_page=100')
            r.raise_for_status()
        except requests.RequestException as req_exception:
            print(f'Error: {req_exception}')
            sys.exit(1)

        try:
            json = r.json()
            meta = json['meta']
            players = json['data']

            for player in players:
                Player.objects.create(
                    id=player['id'],
                    first_name=player['first_name'],
                    last_name=player['last_name'],
                    team=Team.objects.get(pk=player['team']['id'])
                )

            if meta['current_page'] == meta['total_pages']:
                break
        except KeyError as key_error:
            print(f'Error: {key_error}')
            sys.exit(1)
