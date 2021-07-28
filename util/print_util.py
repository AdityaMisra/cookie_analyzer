from typing import List


class PrintUtil:

    @staticmethod
    def print_to_new_line(print_list: List[str]) -> None:
        """
        Print each item of the list in a new line
        :param print_list: List of strings
        :return: None
        """

        for item in print_list:
            print(item)
