from solutions.point_4.constants import *
from solutions.point_4.searching import *
from solutions.point_4.sorting import radix_sort

if __name__ == '__main__':
    list1 = ExpensesList()
    list1.append(ExpensesType.HEALTH, 23, "1/12/22")
    list1.append(ExpensesType.DWELLING, 24, "2/12/22")
    list1.append(ExpensesType.FOOD, 23, "30/12/22")
    list1.append(ExpensesType.EDUCATION, 13, "12/12/24")
    list1.append(ExpensesType.DWELLING, 23, "23/3/24")
    list1.append(ExpensesType.DWELLING, 24, "13/12/22")
    list1.append(ExpensesType.FOOD, 23, "5/5/24")
    list1.append(ExpensesType.EDUCATION, 13, "11/11/24")

    print(list1)

    print("Sorted list: ")
    list2 = radix_sort(list1)
    print(list2)
