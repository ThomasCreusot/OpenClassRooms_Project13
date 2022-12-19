import pytest

from django.urls import reverse, resolve
from django.test import Client

from lettings.models import Address, Letting


@pytest.mark.django_db
def test_letting_list_url():
    """Tests the URL and view name of the page displaying letting objects as a list"""

    address_object_for_testing = Address.objects.create(
        number = 1,
        street = "street_of_testing",
        city = "city_of_testing",
        state = "NY",
        zip_code = 11554,
        country_iso_code = "USA"
    )

    letting_object_for_testing = Letting.objects.create(
        title = "letting_object_for_testing",
        address = address_object_for_testing
    )

    # Generates the URL from the view name
    # author-lettings: namespace in oc_lettings_site/urls.py
    # lettings_index: see lettings/urls.py: from lettings.views import index as lettings_index
    path_index = reverse('author-lettings:lettings_index', current_app="author-lettings")
    assert path_index == "/author-lettings/lettings/"  # checks if URL is right
    assert resolve(path_index).view_name == "author-lettings:lettings_index"  # checks if view name is right


@pytest.mark.django_db
def test_letting_detail_url():
    """Tests the URL and view name of the page displaying letting objects as in details"""

    address_object_for_testing = Address.objects.create(
        number = 1,
        street = "street_of_testing",
        city = "city_of_testing",
        state = "NY",
        zip_code = 11554,
        country_iso_code = "USA"
    )

    letting_object_for_testing = Letting.objects.create(
        title = "letting_object_for_testing",
        address = address_object_for_testing
    )

    # author-lettings : namespace in oc_lettings_site/urls.py
    # letting: from lettings.views import letting
    # letting_id is from: path('lettings/<int:letting_id>/', letting, name='letting')
    path_letting = reverse('author-lettings:letting', current_app="author-lettings", kwargs={'letting_id':1})
    assert path_letting == "/author-lettings/lettings/1/"  # checks if URL is right
    assert resolve(path_letting).view_name == "author-lettings:letting"  # checks if view name is right