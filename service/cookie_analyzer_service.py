from collections import defaultdict
from datetime import datetime
from typing import List

from dto.cookie_details import CookieDetails
from util.file_io import FileIO


class CookieAnalyzer:

    def __init__(self, date_str: str) -> None:
        """
        Constructor of CookieAnalyzer
        :param date_str: date in string format
        """
        
        try:
            self.requested_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as e:
            print("Please enter date in the valid format - ", "YYYY-MM-DD \n")
            raise e

        super().__init__()

    def get_most_active_cookie(self, file_path: str) -> List[str]:
        """
        Returns a list of most active cookie for a particular day
        :param file_path: csv file path
        :return: List of cookie ids
        """

        cookie_details = FileIO.read_csv(file_path)
        if not cookie_details:
            raise Exception("Not able to read the csv file at path - ", file_path)

        counter_map = self._aggregate_cookie(cookie_details)

        return self._get_most_freq_cookie_from_map(counter_map)

    def _aggregate_cookie(self, cookie_details: List[CookieDetails]) -> dict:
        """
        Builds a map which stores the frequency of every cookie
        :param cookie_details: List of cookie details
        :return: Dictionary of cookie_id & frequency
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

    @staticmethod
    def _get_most_freq_cookie_from_map(counter_map: dict) -> List[str]:
        """
        Returns a list of most frequent cookie from the counter map
        :param counter_map: Dictionary of cookie_id & frequency
        :return: List of cookie ids
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
