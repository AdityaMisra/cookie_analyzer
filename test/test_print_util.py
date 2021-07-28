from util.print_util import PrintUtil


class TestPrintUtil:

    def test_print_to_new_line(self, capsys):
        PrintUtil.print_to_new_line(["cookie_1", "cookie_2"])

        out, err = capsys.readouterr()
        assert out == "cookie_1\ncookie_2\n"
