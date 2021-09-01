# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        for item in self.items:

            # Do nothing Sulfuras doesnt depreciate
            if item.name == "Sulfuras, Hand of Ragnaros":
                pass
            # Aged Brie or Backstage passes
            elif (item.name == "Aged Brie" or item.name[0:9] == "Backstage") and (item.sell_in < 50):
                #more than 10 
                if item.sell_in > 10:
                    #item.quality = item.quality + 1
                    item.quality += 1
                    item.sell_in -= 1
                #less than 10 more than 5
                elif item.sell_in <= 10 and item.sell_in > 5:
                    item.quality += 2
                    item.sell_in -= 1
                #less than 5 more than 0
                elif item.sell_in <= 5 and item.sell_in > 0: 
                    item.quality += 3
                    item.sell_in -= 1
                #negative
                else:
                    if item.name == "Aged Brie":
                        item.quality += 3
                        item.sell_in -= 1
                    #Backstage
                    else:
                        item.quality = 0
                        item.sell_in -= 1
            # Conjured Items
            elif item.name[0:8] == "Conjured" and item.quality > 1:
                #-2 normal, -4 past sell in
                #conjured did not pass sell in date
                if item.sell_in >= 0 and item.quality >= 2:
                    item.quality -= 2
                    item.sell_in -= 1
                #
                elif item.sell_in >- 0 and item.quality >= 4:
                    item.quality -= 4
                    item.sell_in -= 1


            #Regular item
            else:
                #print("regular item")
                if item.quality > 0:
                    item.quality = item.quality - 1
                    item.sell_in = item.sell_in - 1





