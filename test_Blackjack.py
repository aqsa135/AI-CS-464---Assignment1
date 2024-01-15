from unittest import TestCase
from Blackjack import get_total

class Test(TestCase):
    def test_get_total(self):
        print(get_total([3,2,1])) # should be 6
        print(get_total([4,11,3])) # should be 18
        print(get_total([6,11,7])) # should be 14


