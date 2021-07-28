import argparse

from service.cookie_analyzer import CookieAnalyzer
from util.print_util import PrintUtil

parser = argparse.ArgumentParser(description='This program returns a list of most active cookies for a given date')

parser.add_argument("-f", default="resources/cookie_log.csv",
                    help="Path of the cookie log file", type=str)

parser.add_argument("-d", default="2018-12-09",
                    help="Date for which we've to fetch the most active cookie",
                    type=str)

args = parser.parse_args()
cookie_analyzer = CookieAnalyzer(args.f, args.d)
PrintUtil.print_to_new_line(cookie_analyzer.get_most_active_cookie())
