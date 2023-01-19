from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    # https://docs.sentry.io/platforms/python/guides/django/
    path('sentry-debug/', views.trigger_error),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('author-lettings/', include('lettings.urls', namespace='author-lettings')),
    path('author-profiles/', include('profiles.urls', namespace='author-profiles')),
]
