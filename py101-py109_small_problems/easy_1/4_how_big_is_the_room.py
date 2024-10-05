'''
Build a program that asks the user to enter the length and width of a room, in meters, 
then prints the room's area in both square meters and square feet.

Note: 1 square meter == 10.7639 square feet

Further Exploration

Modify the program to let the user specify the measurement type 
(meters or feet). Compute the area accordingly and print it and 
its conversion in parentheses.

'''

SQUARE_FEET_IN_A_SQUARE_METER = 10.7639

print("Let's calculate the size of your room.")

def get_unit():
    print("Measure in feet or meters? (f/m)")
    unit = input().lower()

    while not is_valid_unit(unit):
        print("Must be valid unit: m/f")
        unit = input().lower()
    
    match unit:
        case 'm':
            return 'meters'
        case 'f':
            return 'feet'
        

def is_valid_unit(unit):
    return unit and unit[0] in ['m', 'f']

def get_measurement(side, unit):
    print(f"{side} of your room in {unit}: ")
    measurement = input()
    
    while not is_measurement_valid(measurement):
        print("Enter a positive, non-zero number.")
        print(f"{side} of your room in {unit}: ")
        measurement = input()
    
    return float(measurement)

def is_measurement_valid(measurement):
    try:
        float(measurement)
    except ValueError:
        return False
    
    return float(measurement) > 0

def calculate_area(length, width, unit):
    match unit:
        case 'meters':
            area_meters = length * width
            area_feet = area_meters * SQUARE_FEET_IN_A_SQUARE_METER
            return area_feet, area_meters
        case 'feet':
            area_feet = length * width
            area_meters = area_feet / SQUARE_FEET_IN_A_SQUARE_METER
            return area_feet, area_meters
    
def display_area(area_feet, area_meters):
    print(f'The area in square feet is {area_feet:.2f}')
    print(f'The area in square meters is {area_meters:.2f}')
    

def continue_measuring():
    print("Measure another room?")
    choice = input().lower()

    while not choice or choice.lower() not in ('y', 'n'):
        print("Enter (y) or (n).")
        choice = input().lower()
    
    match choice:
        case 'y':
            return True
        case 'n':
            return False

def main():
    continue_program = True
    while continue_program:
        unit = get_unit()

        length = get_measurement('Length', unit)
        width = get_measurement('Width', unit)

        area_feet, area_meters = calculate_area(length, width, unit)

        display_area(area_feet, area_meters)
        
        continue_program = continue_measuring()
main()
