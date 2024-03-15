import sys

# String reversed
def string_reverser(input_str:str):
    # Used slice 
    # [::-1] -> get the last char by char
    reversed_string = input_str[::-1]
    return reversed_string

# Palindrome Char
def palindrome_checker(input_str:str):
    # first step, change string to lower
    input_str = input_str.lower()
    # logic same with string reversed
    # finaly check input_str with new reversed string
    is_palindrome = input_str == input_str[::-1]
    return is_palindrome

# Prime Number with limit
def prime_number_generator(limit:int):
    prime_list = list()
    for num in range(2, int(limit)):
        for divisor in range(2, num):
            if num % divisor == 0:
                break  
        else:
            prime_list.append(num)
    return prime_list


# Function call method
if __name__ == '__main__':
    print(globals()[sys.argv[1]](sys.argv[2]))



# -- README.md

# -- RUN 
# python logicandalgo.py <function> <parameter>

# RUN function string_reverser
# python logicandalgo.py string_reverser "hello"
# Output >> olleh

# RUN function palindrome_checker
# python logicandalgo.py palindrome_checker "heleh"
# output >> True

# RUN function prime_number_generator
# python logicandalgo.py prime_number_generator 10
# Output >> [2, 3, 5, 7]

## ##