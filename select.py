# from pprint import pprint
# import inquirer

# questions = [
#     inquirer.List(
#         "size",
#         message="What size do you need?",
#         choices=["Jumbo", "Large", "Standard", "Medium", "Small", "Micro"],
#     ),
# ]

# answers = inquirer.prompt(questions)
# pprint(answers)

from whaaaaat import prompt, print_json, Separator

questions = [
    {
        "type": "list",
        "name": "theme",
        "message": "What do you want to do?",
        "choices": [
            "Order a pizza",
            "Make a reservation",
            Separator(),
            "Ask for opening hours",
            {"name": "Contact support", "disabled": "Unavailable at this time"},
            "Talk to the receptionist",
        ],
    },
    {
        "type": "list",
        "name": "size",
        "message": "What size do you need?",
        "choices": ["Jumbo", "Large", "Standard", "Medium", "Small", "Micro"],
        "filter": lambda val: val.lower(),
    },
]

answers = prompt(questions)
print(answers)