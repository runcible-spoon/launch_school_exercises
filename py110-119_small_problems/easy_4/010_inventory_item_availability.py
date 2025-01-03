'''
Inventory Item Availability

Building on the previous exercise, write a function that returns True or False based on whether or not an inventory item (an ID number) is available.
As before, the function takes two arguments: an item ID and a list of transactions.

The function should return True only if the sum of the quantity values of the item's transactions is greater than zero.
Notice that there is a movement property in each transaction object. A movement value of 'out' will decrease the item's quantity.

You may (and should) use the transactions_for function from the previous exercise.
'''

def transactions_for(inventory_item, transactions):
    return [transaction
            for transaction in transactions
            if transaction["id"] == inventory_item]

def is_item_available(inventory_item, transactions):
    quant = 0

    for transaction in transactions_for(inventory_item, transactions):
        if transaction['movement'] == 'in':
            quant += transaction['quantity']
        elif transaction['movement'] == 'out':
            quant -= transaction['quantity']

    return quant > 0


transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True
