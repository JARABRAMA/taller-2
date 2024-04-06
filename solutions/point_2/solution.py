from sorting.methods import Sorters


def mode(arr: list[int]) -> int:
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


ls = [1, 1, 1, 2, 2, 3, 5, 5]
print(mode(ls))
