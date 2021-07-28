import pytest

from dto.cookie_details import CookieDetails


class TestCookieDetails:

    def test_cookie_details_success(self):
        cookie = CookieDetails("text_cookie_id", "2018-12-08T09:30:00+00:00")

        assert isinstance(cookie, CookieDetails)

    def test_cookie_details_exception(self):
        with pytest.raises(Exception):
            CookieDetails("text_cookie_id", "2018-14-12T04:35:00+00:00")
