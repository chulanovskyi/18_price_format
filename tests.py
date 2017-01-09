from format_price import format_price
import unittest


class TestFormatPrice(unittest.TestCase):
    def test_invalid_number(self):
        self.assertEqual(format_price('123.123D'), 'NaN')


if __name__ == '__main__':
    unittest.main()
