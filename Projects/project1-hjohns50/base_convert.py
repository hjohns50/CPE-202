#int int -> string
#convert num from base 10 to base b
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    #num is an int that is going to be reduced
    #b is an int that will not change
    #con_dict is a dictionary that contains corresponding value for 10 11 12 13 14 15 
    con_dict = {"10": 'A', "11": 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
    #quotient and remainder are ints
    quotient = num // b
    remainder = num % b
    rem_str = ''
    if quotient == 0:
        if remainder > 9:
            remainder = con_dict[str(remainder)]
        return str(remainder)
    if remainder > 9:
        remainder = con_dict[str(remainder)]
    base = convert(quotient, b)
    rem_str += str(base) + str(remainder)
    return rem_str