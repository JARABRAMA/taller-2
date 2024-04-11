from solutions.point_4.classes import ExpensesList, ExpenseNode


def to_expenses_list(expenses: list[ExpenseNode]) -> ExpensesList:
    result = ExpensesList()  # this method pass from a normal list to a nodal list
    for expense in expenses:
        result.append(expense.get_type(), expense.get_value(), expense.get_date())
    return result


def counting_sort(lista: ExpensesList, exp: int) -> ExpensesList:
    count: list = [0] * 6
    output: list = [0] * lista.size

    bills = lista.get_first()
    while bills is not None:
        index = bills.get_type().get('key') // exp
        count[index % 10] += 1
        bills = bills.get_next()

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    bills = lista.get_first()
    while bills is not None:
        index = bills.get_type().get('key') // exp
        output[count[index % 10] - 1] = bills
        count[index % 10] -= 1
        bills = bills.get_next()

    return to_expenses_list(output)


def max_key(lista: ExpensesList) -> int:
    greatest = lista.get_first()
    expense: ExpenseNode = lista.get_first().get_next()
    while expense is not None:
        if greatest.get_type().get('key') < expense.get_type().get('key'):
            greatest = expense
        expense = expense.get_next()
    return greatest.get_type().get('key')


def radix_sort(list_expenses: ExpensesList) -> ExpensesList:
    greatest = max_key(list_expenses)
    exp = 1
    while greatest // exp > 0:
        list_expenses = counting_sort(list_expenses, exp)
        exp *= 10
    return list_expenses
