import csv
from typing import List, Iterator

from dto.cookie_details import CookieDetails


class FileIO:

    @classmethod
    def read_csv(cls, file_path: str) -> List[CookieDetails]:
        """
        Reads from a csv file
        :param file_path: str: path of the input file
        :rtype: object: returns list of cookie details read from the file
        """

        if not file_path:
            raise Exception("Invalid file path for reading the input")

        try:
            with open(file_path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                cookie_details = cls.parse_csv_file(csv_reader)
        except Exception:
            raise Exception("Error while reading from the input file")

        return cookie_details

    @staticmethod
    def parse_csv_file(csv_reader: Iterator[List[str]]) -> List[CookieDetails]:
        """
        Parses the csv data into CookieDetail objects
        :param csv_reader: Iterator on csv data
        :return: List of CookieDetail objects
        """

        cookie_details = []
        line_count = 0

        for row in csv_reader:
            if line_count > 0:
                cookie_details.append(CookieDetails(row[0], row[1]))
            line_count += 1

        return cookie_details
