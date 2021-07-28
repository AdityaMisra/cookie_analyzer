import argparse

from service.cookie_analyzer_service import CookieAnalyzer
from util.print_util import PrintUtil

parser = argparse.ArgumentParser(description='This program returns a list of most active cookies for a given date')

parser.add_argument("-f", default="resources/cookie_log.csv",
                    help="Path of the cookie log file", type=str)

parser.add_argument("-d", default="2018-12-09",
                    help="Date for which we've to fetch the most active cookie",
                    type=str)

args = parser.parse_args()

print("Printing most freq cookie(s) for the date -> ", args.d)

PrintUtil.print_to_new_line(
    CookieAnalyzer(args.d).get_most_active_cookie(args.f)
)
