from solutions.point4.classes import ExpensesList, ExpensesNode


def to_expenses_list(output: list[ExpensesNode]) -> ExpensesList:
    result = ExpensesList()
    for bill in output:
        result.append(bill.get_value(), bill.get_type(), bill.get_date())
    return result


def counting_sort(lista: ExpensesList) -> ExpensesList:
    count: list = [0] * 5
    output: list = [0] * lista.size

    bills = lista.get_first()
    while bills is not None:
        count[bills.get_type().get('key') - 1] += 1
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
