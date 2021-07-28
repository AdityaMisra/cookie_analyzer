import datetime
from collections import defaultdict

from util.file_io import FileIO
from util.print_util import PrintUtil


class CookieAnalyzer:

    def __init__(self, file_path: str, date_str: str) -> None:
        """
        Constructor of InvitationService
        :param file_path: file path of the cookie log file
        :param date: Date for which we've to fetch the most active cookie
        """

        super().__init__()
        self.file_path = file_path
        # TODO You can assume -d parameter takes date in UTC time zone.
        self.requested_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")

    def get_most_active_cookie(self):

        cookie_details = FileIO.read(self.file_path)

        counter_map = defaultdict(int)

        for cookie in cookie_details:
            if cookie.time.date() == self.requested_date.date():
                counter_map[cookie.cookie_id] += 1

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


if __name__ == "__main__":
    cookie_analyzer = CookieAnalyzer(file_path="../resources/cookie_log.csv", date_str="2018-12-08")
    PrintUtil.print_to_new_line(cookie_analyzer.get_most_active_cookie())