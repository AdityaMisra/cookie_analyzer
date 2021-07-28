import csv
from typing import List

from dto.cookie_details import CookieDetails


class FileIO:

    @staticmethod
    def read(file_path: str) -> List[CookieDetails]:
        """
        Reads from a file
        :param file_path: str: path of the input file
        :rtype: object: returns cookie details read from the file
        """

        if not file_path:
            raise Exception("Invalid file path for reading the input")

        cookie_details = []
        try:
            with open(file_path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count > 0:
                        cookie_details.append(CookieDetails(row[0], row[1]))
                    line_count += 1
        except Exception:
            raise Exception("Error while reading from the input file")

        return cookie_details
