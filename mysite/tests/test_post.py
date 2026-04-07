import pytest
from django.contrib.auth.models import User
from blog.models import Post


@pytest.mark.django_db
def test_post_creation(user):
  post = Post.objects.create(
    title="Hello World",
    slug="hello-world",
    author=user,
    content="Some content here.",
  )
  assert post.pk is not None
  assert post.title == "Hello World"


@pytest.mark.django_db
def test_post_default_status_is_draft(user):
  post = Post.objects.create(
    title="Draft Post",
    slug="draft-post",
    author=user,
    content="Content.",
  )
  assert post.status == 0  # Draft


@pytest.mark.django_db
def test_post_str_returns_title(user):
  post = Post.objects.create(
    title="My Title",
    slug="my-title",
    author=user,
    content="Content.",
  )
  assert str(post) == "My Title"