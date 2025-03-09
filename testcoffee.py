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

# test create_order_num()
    def test_create_order_num_1(self): #assuming the count in order_tracker.txt = 2
        test = functions.create_order_num()
        expected = "002"
        self.assertEqual(test, expected)

    def test_create_order_num_2(self): #assuming the count in order_tracker.txt = 10
        test = functions.create_order_num()
        expected = "010"
        self.assertEqual(test, expected)

    def test_create_order_num_3(self):
        test = functions.create_order_num() # assuming the count in order_tracker.txt = 100
        expected = "100"
        self.assertEqual(test, expected)

if __name__ == '__main__':
    unittest.main()
