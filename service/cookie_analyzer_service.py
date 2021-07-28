from collections import defaultdict
from datetime import datetime
from typing import List

from dto.cookie_details import CookieDetails
from util.file_io import FileIO


class CookieAnalyzer:

    def __init__(self, date_str: str) -> None:
        """
        Constructor of CookieAnalyzer
        :param date_str:
        """
        self.requested_date = datetime.strptime(date_str, "%Y-%m-%d")
        super().__init__()

    def get_most_active_cookie(self, file_path: str):
        """

        :param file_path:
        :return:
        """

        cookie_details = FileIO.read_csv(file_path)
        if not cookie_details:
            raise Exception("Not able to read the csv file at path - ", file_path)

        counter_map = self._aggregate_cookie(cookie_details)

        return self._get_most_freq_cookie_from_map(counter_map)

    def _aggregate_cookie(self, cookie_details: List[CookieDetails]) -> dict:
        """

        :param cookie_details:
        :return:
        """

        counter_map = defaultdict(int)

        for cookie in cookie_details:
            if cookie.time.date() == self.requested_date.date():
                counter_map[cookie.cookie_id] += 1
            elif self.requested_date.date() > cookie.time.date():
                # we don't need to look at the records with date after the requested_date,
                # cookies date in the file is sorted in descending order of dates
                break

        return counter_map

    def _get_most_freq_cookie_from_map(self, counter_map: dict) -> List[str]:
        """

        :param counter_map:
        :return:
        """

        max_count = 0
        most_freq_cookie_list = []

        for cookie_id, count in counter_map.items():
            if count > max_count:
                max_count = count
                most_freq_cookie_list.clear()
                most_freq_cookie_list.append(cookie_id)
            elif count == max_count:
                most_freq_cookie_list.append(cookie_id)

        return most_freq_cookie_list
