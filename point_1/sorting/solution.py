from point_1.utils.list import SLL, SN, HSL
from point_1.sorting.Methods import Sorters


def twolist_toarr(ls1: SLL, ls2: SLL) -> list:
    arr: list[int] = []
    node: SN = ls1.get_first()
    while node is not None:
        arr.append(node.get_data())
        node = node.get_next()
    node = ls2.get_first()
    while node is not None:
        arr.append(node.get_data())
        node = node.get_next()
    return arr


def solution_1(ls1: SLL, ls2: SLL) -> HSL:
    arr = twolist_toarr(ls1, ls2)
    Sorters.selection_sort(arr)
    head_list = HSL(arr)
    return head_list


ls1 = SLL([4, 2, 1, 4, 6, 78])
ls2 = SLL([5, 7, 9, 12, 5, 6])

print(solution_1(ls1, ls2).to_str())
