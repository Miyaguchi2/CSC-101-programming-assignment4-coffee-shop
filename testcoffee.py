import unittest
import functions
import data


class MyTestCase(unittest.TestCase):
# test add_prices() assuming establishment = "ristorante_italia.txt"
    def test_add_prices(self):
        input = [0,1,2]
        expected = 37.97
        test = functions.adding_prices(input)
        self.assertEqual(test, expected)

    def test_add_prices_1(self):
        input = []
        expected = 0.0
        test = functions.adding_prices(input)
        self.assertEqual(test, expected)

    def test_add_prices_2(self):
        input = [-1,0,1,2,1000]
        expected = 37.97
        test = functions.adding_prices(input)
        self.assertEqual(test, expected)

    def test_add_prices_3(self):
        input = [4]
        expected = 13.99
        test = functions.adding_prices(input)
        self.assertEqual(test,expected)

# test add_times() assuming establishment = "ristorante_italia.txt"
    def test_add_times_(self):
        input = [0,1,2]
        expected = 55
        test = functions.adding_time(input)
        self.assertEqual(test, expected)

    def test_add_times_2(self):
        input = []
        expected = 0.0
        test = functions.adding_time(input)
        self.assertEqual(test, expected)

    def test_add_times_3(self):
        input = [-1,0,1,2,1000]
        expected = 55
        test = functions.adding_time(input)
        self.assertEqual(test, expected)

if __name__ == '__main__':
    unittest.main()
