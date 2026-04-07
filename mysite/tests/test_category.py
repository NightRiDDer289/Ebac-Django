import pytest
from blog.models import Category, Post


@pytest.mark.django_db
def test_category_creation():
  category = Category.objects.create(name="Python", slug="python")
  assert category.pk is not None
  assert category.name == "Python"


@pytest.mark.django_db
def test_category_str_returns_name(category):
  assert str(category) == "Django"


@pytest.mark.django_db
def test_post_can_have_multiple_categories(user):
  cat1 = Category.objects.create(name="Python", slug="python")
  cat2 = Category.objects.create(name="Django", slug="django")
  post = Post.objects.create(
      title="My Post", slug="my-post", author=user, content="Content."
  )
  post.categories.add(cat1, cat2)
  assert post.categories.count() == 2
  assert cat1 in post.categories.all()
  assert cat2 in post.categories.all()