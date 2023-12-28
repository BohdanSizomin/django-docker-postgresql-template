import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "adminpass"
ADMIN_EMAIL = "admin@example.com"


@pytest.fixture(autouse=True)
def whitenoise_autorefresh(settings):
    """
    Get rid of whitenoise "No directory at" warning, as it's not helpful when running tests.

    Related:
        - https://github.com/evansd/whitenoise/issues/215
        - https://github.com/evansd/whitenoise/issues/191
        - https://github.com/evansd/whitenoise/commit/4204494d44213f7a51229de8bc224cf6d84c01eb
    """
    settings.WHITENOISE_AUTOREFRESH = True


@pytest.fixture
def admin_client(client, django_user_model):
    """Create an admin user and log in the client."""

    django_user_model.objects.create_superuser(
        username=ADMIN_USERNAME, password=ADMIN_PASSWORD, email=ADMIN_EMAIL
    )
    client.login(username=ADMIN_USERNAME, password=ADMIN_PASSWORD)
    return client


@pytest.mark.django_db
def test_user_create(admin_client):
    response = admin_client.post(
        reverse("admin:%s_%s_add" % (User._meta.app_label, User._meta.model_name)),
        {
            "email": ADMIN_USERNAME,
            "password1": ADMIN_PASSWORD,
            "password2": ADMIN_PASSWORD,
        },
    )
    assert response.status_code == 302  # Assuming a redirect after successful creation
    assert User.objects.count() == 1


# example token test
@pytest.mark.skip(reason="example")
@pytest.mark.django_db
def test_unauthorized_request(api_client, get_or_create_token):
    url = reverse("need-token-url")
    token = get_or_create_token()
    api_client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
    response = api_client.get(url)
    assert response.status_code == 200
