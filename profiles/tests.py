import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from profiles.models import Profile


@pytest.mark.django_db
def test_status_code_200(client):
    path = reverse("profiles:index")
    res = client.get(path)
    assert res.status_code == 200


@pytest.mark.django_db
def test_title_in_index(client):
    path = reverse("profiles:index")
    res = client.get(path)
    res_content = res.content
    assert str(res_content).find("<title>Profiles</title>") > 0


@pytest.mark.django_db
def test_profile_in_profile(client):
    test_user = User.objects.create(username="test_user")
    test_profile = Profile.objects.create(favorite_city="Brunswick",
                                          user_id=test_user.id)
    path = reverse("profiles:profile", kwargs={"username": test_user.username})
    res = client.get(path)
    res_content = res.content
    assert str(res_content).find(test_profile.user.username) > 0
