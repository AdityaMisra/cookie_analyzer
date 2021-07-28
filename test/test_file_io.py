from util.file_io import FileIO


class TestFileIO:
    csv_reader = [['cookie', 'timestamp'],
                  ['AtY0laUfhglK3lC7', '2018-12-09T14:19:00+00:00'], ]

    def test_parse_csv_file(self):
        cooke_details = FileIO.parse_csv_file(self.csv_reader)

        assert len(cooke_details) == 1
