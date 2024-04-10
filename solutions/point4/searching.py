from solutions.point4.classes import ExpensesList


def search_lineal_tipo(lista: ExpensesList, tipo: str) -> ExpensesList:
    result: ExpensesList = ExpensesList()
    bills = lista.get_first()
    while bills is not None:
        if bills.get_type() == tipo:
            result.append(bills.get_type(), bills.get_value(), bills.get_date())
        bills = bills.get_next()
    return result
