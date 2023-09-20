from PyInquirer import prompt
import csv

user_questions = [
    {
        "type": "input",
        "name": "amount",
        "message": "New user - Name: ",
    },
]


def add_user(*args):
    infos = prompt(user_questions)

    with open('users.csv', 'a', newline='') as users_file:
        spam_writer = csv.writer(users_file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spam_writer.writerow([infos.values()])

    print("\n{} has been added to the user list !\n".format(infos['amount']))

    return True
