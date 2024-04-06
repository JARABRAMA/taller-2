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
                if j + 1 < len(arr) and arr[j + 1] < arr[j]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    @staticmethod
    def improved_bubble_sort(arr: list) -> list:
        intercalation = True
        i = len(arr) - 1
        while i > 0 and intercalation:
            intercalation = False
            for i in range(len(arr)):
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
            i -= 1
        return arr

    # the bucket sort only works if the elements of the list to sort are minor than 1 but mayor or equals to cero
    @staticmethod
    def bucket_sort(arr: list[float]) -> list[float]:
        bucket = [[] for _ in range(len(arr))]
        result: list = []
        for i in range(len(arr)):
            bucket[int((arr[i] * len(arr)) // len(arr))].append(arr[i])
        for i in range(len(bucket)):
            Sorters.selection_sort(bucket[i])
        for i in range(len(bucket)):
            for j in range(len(bucket[i])):
                ls = bucket[i]
                result.append(ls[j])
        return result
