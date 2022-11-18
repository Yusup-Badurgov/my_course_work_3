# import pytest
import app


class TestApi:
    """Тестирует API, в соответствии с заданием"""

    post_keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}

    def test_all_posts(self):
        test_client = app.app.test_client()
        response = test_client.get("/api/posts/")
        posts = response.get_json()
        assert response.status_code == 200
        for post in posts:
            assert set(post.keys()) == self.post_keys, "Неправильные ключи у словаря"

    def test_post_pk(self):
        test_client = app.app.test_client()
        response = test_client.get("/api/posts/1")
        post = response.get_json()
        assert response.status_code == 200
        assert set(post.keys()) == self.post_keys, "Неправильные ключи у словаря"
