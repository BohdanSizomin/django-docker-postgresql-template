import pytest
from users.models import User


@pytest.mark.django_db
def test_user_create():
    user = User.objects.create_user(email="test@gmail.com", password="test")
    assert user.email == "test@gmail.com"
