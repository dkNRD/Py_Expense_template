from PyInquirer import prompt
import csv


def read_users():
    users = []
    users_csv = csv.reader(open("users.csv", "r"))
    for user in users_csv:
        users.append({"name": user[0]})

    return users


expense_questions = [
    {
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
    {
        "type": "list",
        "name": "spender_selection",
        "message": "New Expense - Spender: ",
        "choices": read_users(),
    },
    {
        "type": "checkbox",
        "name": "payback_selection",
        "message": "New Expense - Payback: ",
        "choices": read_users()
    },
]


def new_expense(*args):
    infos = prompt(expense_questions)

    if not infos['spender_selection'] in infos['payback_selection']:
        print("\nThe spender must be in the payback users\n")
        return False



    print("Expense Added !\n")
    return True
