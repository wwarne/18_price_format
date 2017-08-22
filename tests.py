import unittest
from format_price import format_price


class TestPrice(unittest.TestCase):

    def test_call_with_empty_argument(self):
        self.assertEqual(format_price(''), None)
        self.assertEqual(format_price(None), None)
        self.assertEqual(format_price([]), None)
        self.assertEqual(format_price({}), None)
        self.assertEqual(format_price(()), None)

    def test_just_one_digit(self):
        price = format_price('1')
        self.assertEqual(price, '1')

    def test_int_two_digits(self):
        price = format_price('10')
        self.assertEqual(price, '10')

    def test_four_digits_number(self):
        price = format_price('1000')
        self.assertEqual(price, '1 000')

    def test_price_remove_zeros(self):
        price = format_price('1000.0000')
        self.assertEqual(price, '1 000')

    def test_price_round(self):
        price = format_price('100.2138')
        self.assertEqual(price, '100.21')

    def test_price_with_endstring(self):
        price = format_price('100\n')
        self.assertEqual(price, '100')

    def test_price_with_endstring_in_beginning(self):
        price = format_price('\n100')
        self.assertEqual(price, '100')

    def test_price_with_letters(self):
        price = format_price('100abc')
        self.assertEqual(price, None)

    def test_price_with_some_unicode(self):
        price = format_price('\n100\t39\N{DOMINO TILE HORIZONTAL-00-00}')
        self.assertEqual(price, None)

    def test_negative_price(self):
        price = format_price('-100')
        self.assertEqual(price, None)

    def test_price_with_leading_dot(self):
        price = format_price('.99')
        self.assertEqual(price, '0.99')

    def test_if_try_convert_object(self):
        price = format_price(object)
        self.assertEqual(price, None)

    def test_infinity(self):
        price = format_price('Infinity')
        self.assertEqual(price, None)

    def test_not_a_number(self):
        price = format_price('NaN')
        self.assertEqual(price, None)

if __name__ == '__main__':
    unittest.main()
