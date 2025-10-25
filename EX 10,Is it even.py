
"""
Exercise 10
Is it even?
ASSESSMENT 1
"""

def main():#defines the main function
    number_input = input("Please enter a number to check for even or odd: ")#input variable used to ask the user to enter a number
    if number_input.isdigit():
        number = int(number_input)#converts input string to a integer
        result = evenORodd(number)#result variable is used to call the evenORodd function
        print(result)#prints the result variable 
    else:#if input is not a valid interger shows error message
        print("Invalid input. Please enter a positive integer.")#prints the error message


def evenORodd(number):#defines the evenORodd function
    if number % 2 == 0:#modulo is used to check if number is divisible by 2
        return f"The number {number} is even"#if number divisible by 2,its an even number
    else:
        return f"The number {number} is odd"#if number not divisible by 2,its an odd number


main()#runs the main function
