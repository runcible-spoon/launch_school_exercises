'''
Create a simple tip calculator. The program should prompt for a bill 
amount and a tip rate. The program must compute the tip, then print 
both the tip and the total amount of the bill. You can ignore input 
validation and assume that the user will enter valid numbers.

Example

What is the bill? 200
What is the tip percentage? 20

The tip is $40.00
The total is $240.00
'''

def get_bill_amount():
    print("Enter bill: ")
    bill = input()

    while not is_input_valid(bill):
        print("Invalid input.\nEnter bill: ")
        bill = input()

    return float(bill)

def is_input_valid(input):
    try:
        float(input)
    except ValueError:
        return False
    
    return float(input) > 0

def get_tip_rate():
    print("Enter tip rate: __%")
    tip_rate = input()

    while not is_input_valid(tip_rate):
        print("Invalid input.\nEnter tip rate as positive number: ")
        tip_rate = input()

    return float(tip_rate) / 100

def calculate_tip(bill, tip_rate):
    return bill * tip_rate

def calculate_total(bill, tip_rate):
    return bill * (1 + tip_rate)

def display_tip(tip):
    print(f"The tip is ${tip:.2f}")

def display_total(total):
    print(f"The total is ${total:.2f}")

def main():
    bill = get_bill_amount()
    tip_rate = get_tip_rate()

    tip = calculate_tip(bill, tip_rate)
    total = calculate_total(bill, tip_rate)

    display_tip(tip)
    display_total(total)

main()
