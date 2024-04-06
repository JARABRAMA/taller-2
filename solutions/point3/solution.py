from sorting.methods import Sorters

cholesterol_hdl = [55, 62, 48, 70, 33, 58, 40, 68, 75, 52, 63, 45, 80, 37, 59, 42, 72, 57, 49, 65]


def to_relative(arr: list[int]) -> list[float]:
    return list(map(lambda x: x / 100, arr))


def to_integer(arr: list[float]) -> list[int]:
    return list(map(lambda x: int(x * 100), arr))


def solution_bucket(arr: list[int]) -> list[int]:
    arr_relative = to_relative(arr)
    result = Sorters.bucket_sort(arr_relative)
    return to_integer(result)


def solution_improved_bubble(arr: list[int]) -> list[int]:
    return Sorters.improved_bubble_sort(arr)


print("Solution by buket sort")
print(solution_bucket(cholesterol_hdl))
print("\nSolution by improved bubble sort")
print(solution_improved_bubble(cholesterol_hdl))
