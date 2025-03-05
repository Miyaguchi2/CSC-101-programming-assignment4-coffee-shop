import unittest
import menu
import data


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

Order = data.Order
    def test_adding_time1(self):

        food_list = ["Mocha Coffee", "Iced Vanilla Coffee", "Vanilla latte", "Mocha Iced coffee", "Matcha milk tea boba", "Milk tea Boba", "Taro milk tea boba", "Birthday cake pop", "Breakfast sandwich", "breakfast Croissan'wich", "Donuts"]
        time_list = [7, 10, 9, 10, 7, 7, 7, 1, 15, 15, 1]
        expected = [7,10,9,10,7,7,7,1,15,15,1]
        result = menu.adding_time(item_list, time_list)
        self.assertEqual(expected, result)














if __name__ == '__main__':
    unittest.main()
