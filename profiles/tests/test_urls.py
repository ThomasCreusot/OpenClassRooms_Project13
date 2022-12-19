import pytest

from django.contrib.auth.models import User

from django.urls import reverse, resolve
from django.test import Client

from profiles.models import Profile


@pytest.mark.django_db
def test_profile_list_url():
    """Tests the URL and view name of the page displaying profile objects as a list"""

    user_object_for_testing = User.objects.create(
        username = "user_username_for_testing",
        password = "user_password_for_testing"
    )

    profile_object_for_testing = Profile.objects.create(
        user = user_object_for_testing,
        favorite_city = "favorite_city_for_testing"
    )

    # Generates the URL from the view name
    # author-profile: namespace in oc_lettings_site/urls.py
    # profiles_index: see profiles/urls.py: from profiles.views import index as profiles_index
    path_index = reverse('author-profiles:profiles_index', current_app="author-profiles")
    assert path_index == "/author-profiles/profiles/"  # checks if URL is right
    assert resolve(path_index).view_name == "author-profiles:profiles_index"  # checks if view name is right


@pytest.mark.django_db
def test_profile_detail_url():
    """Tests the URL and view name of the page displaying profile objects in details"""

    user_object_for_testing = User.objects.create(
        username = "user_username_for_testing",
        password = "user_password_for_testing"
    )

    profile_object_for_testing = Profile.objects.create(
        user = user_object_for_testing,
        favorite_city = "favorite_city_for_testing"
    )

    # author-profiles : namespace in oc_lettings_site/urls.py
    # profiles is from : in urls.py : from profiles.views import profile
    # username is from: path('profiles/<str:username>/', profile, name='profile'),
    path_profile = reverse('author-profiles:profile', current_app="author-profiles", kwargs={'username':1})
    assert path_profile == "/author-profiles/profiles/1/"  # checks if URL is right
    assert resolve(path_profile).view_name == "author-profiles:profile"  # checks if view name is right

