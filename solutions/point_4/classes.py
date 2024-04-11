class ExpenseNode:
    def __init__(self, type: dict, value: int, date: str):
        self._next = None
        self._type = type
        self._value = value
        self._date = date

    def set_next(self, expenses):
        self._next = expenses

    def get_next(self):
        return self._next

    def __str__(self) -> str:
        return f"Expenses: tipo: {self.get_type()}, value: {self.get_value()}, date: {self.get_date()}"

    def get_type(self):
        return self._type

    def get_value(self):
        return self._value

    def get_date(self):
        return self._date


class ExpensesList:
    def __init__(self) -> None:
        self._head = ExpenseNode(dict(), 0, "0/0/0")
        self._last = self.get_head()
        self.size = 0
        self.total_value = 0

    def __str__(self) -> str:
        list_str: str = ""
        node = self.get_first()
        while node is not None:
            list_str += f"[{node.__str__()}]\n"
            node = node.get_next()
        return list_str

    def append(self, tipo: dict, value: int, date: str):
        node = ExpenseNode(tipo, value, date)
        if self.size == 0:
            self.get_head().set_next(node)
            self.set_last(node)
        else:
            self.get_last().set_next(node)
            self.set_last(node)
        self.size += 1
        self.total_value += value

    def get_head(self):
        return self._head

    def get_last(self):
        return self._last

    def set_last(self, node: ExpenseNode):
        self._last = node

    def get_first(self) -> ExpenseNode:
        return self.get_head().get_next()
