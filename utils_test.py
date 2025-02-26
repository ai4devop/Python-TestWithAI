import unittest
from datetime import datetime
from utils import formatDate, parseDate, formatDateWithPattern, formatDateTime, parseDateTime, formatDateTimeWithPattern

class TestUtils(unittest.TestCase):

    #========================= TDD ============================

    def test_format_date_valid_date(self):
        date = datetime(2023, 10, 16)  # October 16, 2023
        self.assertEqual(formatDate(date), "2023-10-16")

    def test_parse_date_valid_date(self):
        date = "2023-01-05"  # January 5, 2023
        self.assertEqual(parseDate(date), datetime(2023, 1, 5))

    def test_format_date_with_pattern(self):
        date = datetime(2024, 10, 28)  # October 28, 2024
        self.assertEqual(formatDateWithPattern(date, "dd/MM/yyyy"), "28/10/2024")
        self.assertEqual(formatDateWithPattern(date, "yyyy-MM-dd"), "2024-10-28")

    #========================= Test by description ============================

    def test_format_date_time_valid_date_time(self):
        # TODO :: Test to be implemented
        pass

    def test_parse_date_time_valid_date_time(self):
        # TODO :: Test to be implemented
        pass

    #========================= Test by code ============================

    def test_format_date_time_with_pattern(self):
        # TODO :: Test to be implemented
        pass

if __name__ == '__main__':
    unittest.main()