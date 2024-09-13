'''
Build a program that asks the user to enter the length and width of a room, in meters, 
then prints the room's area in both square meters and square feet.

Note: 1 square meter == 10.7639 square feet
'''


def room_size(length_meters, width_meters):
    area_meters = float(length_meters) * float(width_meters)
    area_feet = round(area_meters * 10.7639, 2)
    print(f'The area in square meters is {area_meters}')
    print(f'The area in square feet is {area_feet}')


print("Length in meters: ")
length_meters = input()

print("Width in meters: ")
width_meters = input()

room_size(length_meters, width_meters)


'''
Further Exploration

Modify the program to let the user specify the measurement type 
(meters or feet). Compute the area accordingly and print it and 
its conversion in parentheses.
'''
print("Let's calculate the size of your room.")


def valid_unit(input):
    return input and input[0] in ['m', 'f']

def get_unit():
    print("Measure in feet or meters? (f/m)")
    unit = input().lower()

    while not valid_unit(unit):
        print("Enter unit: (f)eet or (m)eters.")
        unit = input().lower()

    if unit[0] == 'm':
        return 'meters'
    else:
        return 'feet'


def valid_measurement(input):
    try:
        float(input)
    except ValueError:
        print("Enter a positive, non-zero number.")
        return False
    
    return float(input) > 0

def get_measurement(measure, unit):
    measurement = input(f"Enter the {measure} of the room in {unit}: ")
    
    while not valid_measurement(measurement):
        measurement = input("Is this text necessary?")
    
    return float(measurement)


def calculate_area(length, width):
    area = length * width
    return area
    

# conversion factor from square feet to square meters
SQ_FEET_TO_SQ_METERS = 10.7639

def convert(unit, area):
    if unit == 'meters':
        area *= SQ_FEET_TO_SQ_METERS
        print('Converted area: ', area)   
        return area
    else:
        return area
    

def print_area(unit, area):
    print(f"Room is {area:.2f} square {unit}.")




def main():
    unit = get_unit()
    length = get_measurement('length', unit)
    width = get_measurement('width', unit)

    converted_area = convert(unit, calculate_area(length, width))

    print_area(unit, converted_area)
    
main()
