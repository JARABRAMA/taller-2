class Sorters:
    @staticmethod
    def insertion_sort(arr: list[int]) -> list[int]:
        for i in range(len(arr)):
            p = arr[i]
            j = i - 1
            while j > -1 and p < arr[j]:
                arr[j + 1] = arr[j]
                j = j - 1
            arr[j + 1] = p
        return arr

    # build an algorithm that sort from mayor to minor
    @staticmethod
    def reverse_insertion_sort(arr: list[int]) -> list[int]:
        for i in range(len(arr)):
            p = arr[i]
            j = i - 1
            while j > -1 and p > arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = p
        return arr

    @staticmethod
    def selection_sort(arr: list[int]) -> list[int]:
        for i in range(len(arr)):
            least = i
            for j in range(i, len(arr)):
                if arr[least] > arr[j]:
                    least = j
            arr[i], arr[least] = arr[least], arr[i]
        return arr

    @staticmethod
    def bubble_sort(arr: list[int]) -> list[int]:
        for i in range(len(arr) - 1):
            for j in range(len(arr)):
                print(arr)
                if j + 1 < len(arr) and arr[j + 1] < arr[j]:
                    # intercalation
                    # print(f"element in j: {arr[j]}, element in j + 1: {arr[j + 1]}")
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    @staticmethod
    def improved_bubble_sort(arr: list[int]) -> list[int]:
        intercalation = True
        i = len(arr) - 1
        while i > 0 and intercalation:
            intercalation = False
            for i in range(len(arr)):
                print(arr)
                if i < len(arr) - 1:
                    if arr[i] > arr[i + 1]:
                        intercalation = True
                        temp = arr[i]
                        arr[i] = arr[i + 1]
                        arr[i + 1] = temp
            i = i - 1
        return arr

    @staticmethod
    def shaker_sort(arr: list[int]) -> list[int]:
        i: int = len(arr) // 2  # this method only need the middle of the length of the list to sort it
        swap: bool = True
        init: int = 0
        final: int = len(arr) - 1
        while i > - 1 and swap:
            swap = False
            for j in range(init, final):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swap = True
            final -= 1

            for j in range(final, init, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    swap = True

            init += 1
        return arr
