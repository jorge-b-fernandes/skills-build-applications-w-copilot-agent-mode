from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', members=[])
        dc = Team.objects.create(name='dc', members=[])

        # Create users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User.objects.create(email='captain@marvel.com', name='Captain America', team='marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='dc'),
            User.objects.create(email='superman@dc.com', name='Superman', team='dc'),
        ]
        marvel.members = [user.name for user in users if user.team == 'marvel']
        dc.members = [user.name for user in users if user.team == 'dc']
        marvel.save()
        dc.save()

        # Create activities
        Activity.objects.create(user='Iron Man', type='run', duration=30, date='2025-12-01')
        Activity.objects.create(user='Captain America', type='cycle', duration=45, date='2025-12-02')
        Activity.objects.create(user='Batman', type='swim', duration=25, date='2025-12-03')
        Activity.objects.create(user='Superman', type='run', duration=60, date='2025-12-04')

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=75)
        Leaderboard.objects.create(team='dc', points=85)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
