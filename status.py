from PyInquirer import prompt
import csv


def uwu():
    expenses_csv = csv.reader(open("expense_report.csv", "r"))

    owes = []
    for expense in expenses_csv:
        price = float(expense[0])
        spender = expense[2]
        payback_users = expense[3][1:-1].split(", ")

        for i in range(len(payback_users)):
            payback_users[i] = payback_users[i][1:-1]

        for user in payback_users:
            if user == spender:
                continue
            amount = price / len(payback_users)
            owes.append({"user": user, "amount": amount, "to": spender})

    simplified_owes = []
    for owe in owes:
        for simplified_owe in simplified_owes:
            if simplified_owe['user'] == owe['to'] and simplified_owe['to'] == owe['user']:
                if simplified_owe['amount'] > owe['amount']:
                    simplified_owe['amount'] -= owe['amount']
                    owe['amount'] = 0
                elif simplified_owe['amount'] < owe['amount']:
                    owe['amount'] -= simplified_owe['amount']
                    simplified_owe['amount'] = 0
                else:
                    simplified_owe['amount'] = 0
                    owe['amount'] = 0
            if simplified_owe['amount'] == 0:
                simplified_owes.remove(simplified_owe)

        if owe['amount'] > 0:
            simplified_owes.append(owe)

    simplified_owes_in_plain_text = []
    for simplified_owe in simplified_owes:
        simplified_owes_in_plain_text.append(f"{simplified_owe['user']} owes {simplified_owe['to']} {simplified_owe['amount']}")

    return simplified_owes_in_plain_text


status_questions = [
    {
        "type": "list",
        "name": "status_selection",
        "message": "Show Status - User: ",
        "choices": uwu(),
    }
]

def status(*args):
    infos = prompt(status_questions)
    return True
