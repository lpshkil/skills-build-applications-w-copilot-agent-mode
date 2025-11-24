"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import TeamViewSet, UserViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet, api_root
import os


router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'users', UserViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardViewSet)

# Patch DRF reverse to use codespace host if present
from rest_framework.reverse import reverse as drf_reverse
def codespace_reverse(viewname, args=None, kwargs=None, request=None, format=None, **extra):
    url = drf_reverse(viewname, args=args, kwargs=kwargs, request=request, format=format, **extra)
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name and request is not None:
        url = url.replace('http://localhost:8000', f'https://{codespace_name}-8000.app.github.dev')
        url = url.replace('http://127.0.0.1:8000', f'https://{codespace_name}-8000.app.github.dev')
    return url
import sys
sys.modules['octofit_tracker.urls_reverse'] = type('urls_reverse', (), {'reverse': codespace_reverse})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', api_root, name='api-root'),
]
