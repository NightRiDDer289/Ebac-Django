import pytest
from django.contrib.auth.models import User
from blog.models import Category

@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", password="pass")

@pytest.fixture
def category(db):
  return Category.objects.create(name="Django", slug="django")