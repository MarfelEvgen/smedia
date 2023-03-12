import pytest

@pytest.mark.django_db
def test_title():
    article = Post.object.create(title='article1')
    assert article.title == 'article1'