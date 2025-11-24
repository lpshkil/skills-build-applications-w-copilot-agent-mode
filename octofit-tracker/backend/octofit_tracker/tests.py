from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team', universe='Test')
        self.assertEqual(str(team), 'Test Team')

    def test_create_user(self):
        team = Team.objects.create(name='Test Team', universe='Test')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(str(user), 'Test User')

    def test_create_activity(self):
        team = Team.objects.create(name='Test Team', universe='Test')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        activity = Activity.objects.create(user=user, type='Test', duration=10, date='2025-01-01')
        self.assertIn('Test', str(activity))

    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', difficulty='Easy')
        self.assertEqual(str(workout), 'Test Workout')

    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team', universe='Test')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        lb = Leaderboard.objects.create(user=user, score=10, rank=1)
        self.assertIn('Test User', str(lb))
