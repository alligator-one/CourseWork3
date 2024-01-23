from utils import *

executed = get_exeсs(load_json())
operations = sort_dates(executed)
dates = date_format(operations)
card_number = hide_card_number(operations)
amount_number = hide_amount_number(operations)

for operation in range(len(operations)):
    print(f"{dates[operation]} {operations[operation]['description']}")
    print(f"{card_number[operation]} -> Счет {amount_number[operation]}")
    print(f"{operations[operation]['operationAmount']['amount']} {operations[operation]['operationAmount']['currency']['name']}\n")