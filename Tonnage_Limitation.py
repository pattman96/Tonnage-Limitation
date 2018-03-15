# Import the functions that calculate the separate brackets
from TL_Functions import *

############################################################
# Get user to set vessel name
vessel_name = input('Enter vessel name:')

# Get user to set vessel weight
weight = int(input('Enter vessel weight in tons:'))

# Print explanation message to user
print('The choice of limitation conventions includes: the Limitation Convention of 1957 (LC1957),'
      '\nthe Limitation Convention of 1976 (LC1976), or the Limitation Convention of 1996 (LC1996).'
      '\nPlease type your choice in e.g. LC1957')

# Get user to type in which convention applies
convention = input('Enter convention:')

# Get user to set if PI or death has occurred
print('Has death or personal injury occurred?'
      '\n If yes, type 1, if no, type 0')
# Convert to Boolean
PI = bool(int(input('Enter whether PI/death occurred:')))

#Store in a dictionary
ship_dict = {vessel_name: weight}
############################################################

def compute_limit(ship_dict, PI, convention):
    if PI == True and convention == 'LC1957':
        for k in ship_dict.keys():
            print(ship_dict[k] * 206.67)

    elif PI == False and convention == 'LC1957':
        for k in ship_dict.keys():
            print(ship_dict[k] * 66.67)

    elif PI == True and convention == 'LC1976':
        PI_1976(ship_dict)

    elif PI == False and convention == 'LC1976':
        No_PI_1976(ship_dict)

    elif PI == True and convention == 'LC1996':
        PI_1996(ship_dict)

    elif PI == False and convention == 'LC1996':
        No_PI_1996(ship_dict)

############################################################

compute_limit(ship_dict, PI, convention)




