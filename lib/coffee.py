#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return getattr(self, "_size", None)

    @size.setter
    def size(self, value):
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
            self._size = None

    @property
    def price(self):
        return getattr(self, "_price", None)

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)):
            self._price = value
        else:
            print("price must be a number")
            self._price = None

    def tip(self):
        self.price += 1
        print("This coffee is great, here’s a tip!")