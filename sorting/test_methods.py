from unittest import TestCase

from sorting.methods import Sorters


class TestSorters(TestCase):
    ls_integers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
    ls_float = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0, 0.12, 0.34, 0.98, 0.001, 0.01, 0.112]

    def test_shaker_sort(self):
        print(Sorters.shaker_sort(self.ls_integers))

    def test_bucket_sort(self):
        print(Sorters.bucket_sort(self.ls_float))
