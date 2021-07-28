from unittest.mock import MagicMock

import pytest

from dto.cookie_details import CookieDetails
from service.cookie_analyzer_service import CookieAnalyzer
from util.file_io import FileIO


class TestCookieAnalyzer:
    cookie_details = [CookieDetails('AtY0laUfhglK3lC7', '2018-12-09T14:19:00+00:00'),
                      CookieDetails('SAZuXPGUrfbcn5UA', '2018-12-09T10:13:00+00:00'),
                      CookieDetails('5UAVanZf6UtGyKVS', '2018-12-09T07:25:00+00:00'),
                      CookieDetails('AtY0laUfhglK3lC7', '2018-12-09T06:19:00+00:00'),
                      CookieDetails('SAZuXPGUrfbcn5UA', '2018-12-08T22:03:00+00:00'),
                      CookieDetails('4sMM2LxV07bPJzwf', '2018-12-08T21:30:00+00:00'),
                      CookieDetails('fbcn5UAVanZf6UtG', '2018-12-08T09:30:00+00:00'),
                      CookieDetails('4sMM2LxV07bPJzwf', '2018-12-07T23:30:00+00:00'), ]

    cookie_log_file_path = "resources/cookie_log.csv"

    counter_map_with_single_result = {
        "AtY0laUfhglK3lC7": 2,
        "SAZuXPGUrfbcn5UA": 1,
        "5UAVanZf6UtGyKVS": 1
    }

    counter_map_with_multiple_result = {
        "AtY0laUfhglK3lC7": 2,
        "SAZuXPGUrfbcn5UA": 2,
        "5UAVanZf6UtGyKVS": 1
    }

    cookie_single_result = ["AtY0laUfhglK3lC7"]

    cookie_multiple_result = ["AtY0laUfhglK3lC7", "SAZuXPGUrfbcn5UA"]

    def test_aggregate_cookie(self):
        assert CookieAnalyzer("2018-12-09")._aggregate_cookie(
            self.cookie_details) == self.counter_map_with_single_result

    def test_get_most_freq_cookie_from_map_with_single_cookie(self):
        most_freq_cookie_list = CookieAnalyzer("2018-12-09") \
            ._get_most_freq_cookie_from_map(self.counter_map_with_single_result)

        assert len(most_freq_cookie_list) == len(self.cookie_single_result)
        assert all([a == b for a, b in zip(most_freq_cookie_list, self.cookie_single_result)])

    def test_get_most_freq_cookie_from_map_with_multiple_cookies(self):
        most_freq_cookie_list = CookieAnalyzer("2018-12-09"). \
            _get_most_freq_cookie_from_map(self.counter_map_with_multiple_result)

        assert len(most_freq_cookie_list) == len(self.cookie_multiple_result)
        assert all([a == b for a, b in zip(most_freq_cookie_list, self.cookie_multiple_result)])

    def test_get_most_active_cookie(self):
        cookie_analyzer = CookieAnalyzer("2018-12-09")

        FileIO.read_csv = MagicMock(return_value=self.cookie_details)

        cookie_analyzer._aggregate_cookie = MagicMock(return_value=self.counter_map_with_single_result)
        cookie_analyzer._get_most_freq_cookie_from_map = MagicMock(return_value=self.cookie_single_result)

        most_freq_cookie_list = cookie_analyzer.get_most_active_cookie(self.cookie_log_file_path)

        assert len(most_freq_cookie_list) == len(self.cookie_single_result)
        assert all([a == b for a, b in zip(most_freq_cookie_list, self.cookie_single_result)])

    def test_get_most_active_cookie_with_exception(self):
        cookie_analyzer = CookieAnalyzer("2018-12-09")
        FileIO.read_csv = MagicMock(return_value=None)

        with pytest.raises(Exception):
            cookie_analyzer.get_most_active_cookie(self.cookie_log_file_path)

