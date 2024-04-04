# Simple node 
class SN:
    def __init__(self, data) -> None:
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_next(self):
        return self._next

    def set_next(self, next):
        self._next = next


# simple link list 
class SLL:
    def __init__(self, arr: list = None) -> None:
        self._first = None
        self._last = None
        self.size = 0
        if arr is not None:
            for i in range(len(arr)):
                self.append(arr[i])

    def append(self, data):
        node = SN(data)
        if self.size == 0:
            self.set_first(node)
            self.set_last(node)
        else:
            self.get_last().set_next(node)
            self.set_last(node)
        self.size += 1

    def get_first(self):
        return self._first

    def set_first(self, first: SN):
        self._first = first

    def get_last(self):
        return self._last

    def set_last(self, last: SN):
        self._last = last

    def to_str(self) -> str:
        result: str = ''
        node = self.get_first()
        while node is not None:
            result += f'{node.get_data()} -> '
            node = node.get_next()
        return result


# head simple link list 
class HSL:
    def __init__(self, arr: list = None) -> None:
        self._head = SN(0)
        self._last = self.get_head()
        self.size = 0
        if arr is not None:
            for i in range(len(arr)):
                self.append(arr[i])

    def append(self, data):
        node = SN(data)
        if self.size == 0:
            self.get_head().set_next(node)
            self.set_last(node)
        else:
            self.get_last().set_next(node)
            self.set_last(node)
        self.size += 1

    def to_str(self) -> str:
        result: str = ""
        node = self.get_first()
        while node is not None:
            result += f'{node.get_data()} -> '
            node = node.get_next()
        return result

    def get_head(self):
        return self._head

    def get_last(self):
        return self._last

    def set_last(self, node: SN):
        self._last = node

    def get_first(self) -> SN:
        return self.get_head().get_next()
