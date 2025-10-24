"""
EX6 with optional requirements
Brute Force Attack
ASSESSMENT 1
"""
correctPassword="12345"#defines the correct password

max_attempts=5#number of max attemps
attempts=0#starting number of attempts
while attempts < max_attempts:#while loop used to repeat the same statement as long as condition is satisfied 0<5 
    question=input("Enter your password: ")#question in the while loop
    
    if question==correctPassword:#if statement  is used to test a condition
        print("Correct Password, Access Granted!")#shows the output if condition is statisfied
        break#breaks the loop if answer is right 
    else:#else statement used to test other condition
        attempts+=1#increases the number of attempts each time
        remaining_attempts=max_attempts-attempts#the ammount of remaining attempts=max attemps-attempts
        if remaining_attempts>=1:#if staetment used to run the condition as long as remaining attempts > or =1
            print("incorrect password you have" ,remaining_attempts,"attempts left")#shows the output if remaining_attempts>=1
        else:#else condition used to run if remaining_attempts<1
            print("Maximum number of attempts reached, AUTHORITIES HAVE BEEN ALLERTED!")#shows the output if remaining_attempts<1
            