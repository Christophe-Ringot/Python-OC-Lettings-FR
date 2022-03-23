from django.urls import reverse


def test_status_code_200(client):
    path = reverse("index")
    res = client.get(path)
    assert res.status_code == 200


def test_title_in_index(client):
    path = reverse("index")
    res = client.get(path)
    res_content = res.content
    assert str(res_content).find("<title>Holiday Homes</title>") > 0
