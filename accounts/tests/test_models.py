import pytest
from ..models import User

pytestmark = pytest.mark.django_db


def test_create_user():
    user = User.objects.create_user(
        username="user_test",
        email="user@test.com",
        password="passW0rd",
    )

    assert user.username == "user_test"
    assert user.email == "user@test.com"
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser
