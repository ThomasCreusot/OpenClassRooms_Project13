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


def test_index_view():
    """Tests the view content of the index page.
    Specifications : as each website page contains a title, each test must verify it in the
    HTML answer. Response status code il also tested."""

    client = Client()  # Equivalent to a simplified web browser

    path_index = reverse('index')
    response = client.get(path_index)
    content = response.content.decode()
    print(content)
    expected_content = "<h1>Welcome to Holiday Homes</h1>"

    assert content.find(expected_content) != -1
    assert response.status_code == 200
