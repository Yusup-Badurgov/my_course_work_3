import pytest
from post_view import View


class TestView:
    """Тестирует класс View """

    def test_get_views(self):
        view = View()
        view.get_add_view(1)
        assert view.get_views() == {1}, "Error return View"

    def test_get_verify_true(self):
        view = View()
        view.get_add_view(2)
        assert view.get_verify_view(2) is True, "Error in View True"

    def test_get_verify_false(self):
        view = View()
        view.get_add_view(2)
        assert view.get_verify_view(3) is False, "Error in View false"
