from sorting.methods import Sorters
from utils.list import SLL


def get_mode(arr: list[int]) -> int:
    matrix = [[] for _ in range(len(arr))]
    Sorters.selection_sort(arr)
    element: int = arr[0]
    j = 0
    for i in range(len(arr)):
        if element != arr[i]:
            j += 1
            element = arr[i]
        matrix[j].append(element)
    mayor: int = 0
    for i in range(len(matrix) - 1):
        if len(matrix[i + 1]) > len(matrix[mayor]):
            mayor = i + 1

    return matrix[mayor][0]


def solution_insertion(arr: list[int], mode: int):
    result = []
    for i in range(len(arr)):
        if arr[i] < mode:
            result.append(arr[i])
    return SLL(Sorters.insertion_sort(result))


def solution_shaker(arr: list[int], mode: int):
    result = []
    for i in range(len(arr)):
        if arr[i] < mode:
            result.append(arr[i])
    return SLL(Sorters.shaker_sort(result))


ls = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6]
mode = get_mode(ls)
print(f'mode: {mode}\n')
print("solution by insertion")
print(solution_insertion(ls, mode).to_str())
print('\nsolution by shaker')
print(solution_shaker(ls, mode).to_str())
