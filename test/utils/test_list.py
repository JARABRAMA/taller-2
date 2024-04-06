from unittest import TestCase

from utils.list import SLL


class Test(TestCase):
    arr1: list = [1, 23, 4, 5]

    def test_sll(self):
        ls1: SLL = SLL(self.arr1)
        print(ls1.to_str())

    def test_lnc(self):
        self.fail()
