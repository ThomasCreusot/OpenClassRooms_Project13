import pytest

from django.urls import reverse, resolve
from django.test import Client


def test_index_url():
    """Tests the URL and view name of the index page"""

    # Generates the URL from the view name
    # author-lettings: namespace in oc_lettings_site/urls.py
    # lettings_index: see lettings/urls.py: from lettings.views import index as lettings_index
    path_index = reverse('index')
    assert path_index == "/"  # checks if URL is right
    assert resolve(path_index).view_name == "index"  # checks if view name is right
