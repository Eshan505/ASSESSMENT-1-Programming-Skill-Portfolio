
"""
EX3 with advanced requirements
ASSESSMENT 1
Biography
"""
Name=str(input("Enter your full name: "))#Name variable used to store user input as string
Home=str(input("Enter your hometown: "))#Home variable used to store user input as string


while True:# while loop Keeps asking for age until the user types a valid number.

    Age = input("Enter your age: ")#asks user for their age
    if Age.isdigit():#we use the function isdigit() to make sure the input is integer
        age = int(Age)#shows age if its integer
        break#breaks loop once done
    else:#else used to constantly show error message if input is a string
        print("Invalid input. Please enter your age as a number.")

    


dict={"name": Name,
    "hometown": Home,
    "age": Age }#dictionary storing the name hometown and age values and keys

for value in dict.values():
    print(value) #for loop used to print all values in the dictionary on seperate lines
    
"""   
Try giving both your first and second name when asked for your name. What happens? 
How can you handle multiple words in Python? 
ans= Python treats the full input as a single string, even if it contains spaces.
"""

"""
Test the program by entering a string value for age (e.g., "twenty"). What happens?
How can you prevent this issue?
ans=it shows error as the input is not an integer and its a string so to prevent this issue 
We could use the function isdigit() to ensure that the input contains only digits
"""