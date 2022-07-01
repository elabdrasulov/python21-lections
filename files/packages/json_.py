import json


with open('test.json', 'w') as file:
    dict_ = {
        'products':  [
            {
                'id': 1,
                'name':'snickers',
                'price': 45,
            },
            {
                'id': 2,
                'name': 'bounty',
                'price': 45
            }
        ]
            }

    # print(dict_)
    json.dump()