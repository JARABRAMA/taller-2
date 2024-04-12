from solutions.point_4.classes import ExpensesList, ExpenseNode
from solutions.point_4.sorting import radix_sort


def lineal_search(lista: ExpensesList, tipo: str, date: str) -> ExpensesList:
    result: ExpensesList = ExpensesList()
    bill = lista.get_first()
    while bill is not None:
        bill_type = bill.get_type().get('type')
        print(f'bill of date {bill.get_date()} and type {bill_type}\n')
        if bill.get_type() == tipo and bill.get_date() == date:
            result.append(bill.get_type(), bill.get_value(), bill.get_date())
            print(f'{bill} is added to the list')
            print(f'list: \n{result}')
        bill = bill.get_next()
        print('\n')
    return result


def to_default_list(expenses_list: ExpensesList) -> list[ExpenseNode]:
    result = []
    node = expenses_list.get_first()
    while node is not None:
        result.append(node)
        node = node.get_next()
    return result


def binary_search(expenses: ExpensesList, tipo: dict, date: str) -> ExpensesList:
    result: ExpensesList = ExpensesList()
    expenses: list[ExpenseNode] = to_default_list(radix_sort(expenses))
    initial: int = 0
    final = len(expenses)
    target = tipo.get('key')
    while final > initial:
        compare = (initial + final) // 2
        if target == expenses[compare].get_type().get('key'):
            index = compare
            while (index < len(expenses) and target == expenses[index].get_type().get('key') and date == expenses[index]
                    .get_date()):
                result.append(expenses[index].get_type(), expenses[index].get_value(), expenses[index].get_date())
                index += 1
            index = compare - 1

            while index > -1 and target == expenses[index].get_type().get('key') and date == expenses[index].get_date():
                result.append(expenses[index].get_type(), expenses[index].get_value(), expenses[index].get_date())
                index -= 1
            break
        elif target > expenses[compare].get_type().get('key'):
            initial = compare
        else:
            final = compare
    return result
