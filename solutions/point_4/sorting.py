from solutions.point_4.classes import ExpensesList, ExpensesNode


def to_expenses_list(expenses: list[ExpensesNode]) -> ExpensesList:
    result = ExpensesList()  # this method pass from a normal list to a nodal list
    for expense in expenses:
        result.append(expense.get_type(), expense.get_value(), expense.get_date())
    return result


def counting_sort(lista: ExpensesList) -> ExpensesList:
    count: list = [0] * 6
    output: list = [0] * lista.size

    bills = lista.get_first()
    while bills is not None:
        count[bills.get_type().get('key')] += 1
        bills = bills.get_next()

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    bills = lista.get_first()
    while bills is not None:
        p = count[bills.get_type().get('key')] - 1
        output[p] = bills
        count[bills.get_type().get('key')] -= 1
        bills = bills.get_next()

    return to_expenses_list(output)
