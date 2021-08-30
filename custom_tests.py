from __future__ import print_function

from gilded_rose import *
import unittest
from item import Item

class GildedRoseTest(unittest.TestCase):

    def setUp(self):
        self.items = []

    def test_regular_items(self):
        self.items.append(Item("Black Lotus", 5, 6))
        GildedRose(self.items).update_quality()
        expected = {'sell_in': 4, 'quality': 5}
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])
        self.assertEqual(item.sell_in, expected['sell_in'])
    
    def test_items_appreciating(self):
        self.items.append(Item("Aged Brie", 15, 35))
        self.items.append(Item("Backstage passes to a TAFKAL80ETC concert", 15, 30))
        GildedRose(self.items).update_quality()
        expected = [
              {'sell_in': 14, 'quality': 36},
              {'sell_in': 14, 'quality': 31},
            ]

        for index, expectation in enumerate(expected):
            item = self.items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.sell_in, expectation['sell_in'])

    def test_items_appreciating_days_5_or_less(self):
        self.items.append(Item("Aged Brie", 4, 11))
        self.items.append(Item("Backstage passes to a TAFKAL80ETC concert", 5, 15))
        GildedRose(self.items).update_quality()
        expected = [
            {'sell_in': 3, 'quality': 14},
            {'sell_in': 4, 'quality': 18},
        ]

        for index, expectation in enumerate(expected):
            item = self.items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.sell_in, expectation['sell_in'])


if __name__ == "__main__":
    print("Custom Tests")
    unittest.main()