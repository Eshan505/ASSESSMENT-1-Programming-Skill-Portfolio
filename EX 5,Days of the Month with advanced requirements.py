
"""
EX5 with advanced requirements
Days of the Month
ASSESSMENT 1
"""
dict={1:31,
      2:28,
      3:31,
      4:30,
      5:31,
      6:30,
      7:31,
      8:31,
      9:30,
      10:31,
      11:30,
      12:31 }#dictionary the months are keys and no. of days are values

question=int(input("Enter your month number: "))#asks the month number

if question <=12:#if month number is less than or equal to 12 it prints the output
    print(dict[question],"days")#this prints the output value of how many days in that specific month
    if question==2:#nested if function to specify if the first criteria is right then check this criteria as well
        leap_question=input("Is it a leap year? (yes/no): ")#asks if the 2nd month(february) is a leap year 
        if leap_question == "yes":#if it is a leap year
            print("February has 29 days in leap year")#prints the output saying february has 29 days instead of 28 days
        else:#else function used so that if it isnt a leap year it prints that february has 28 days
            print("February has 28 days")#prints that february has 28 days
else:#if the month number>12 runs this criteria 
    print("Error!",question,"is not a valid month number")#this output is displayed if month no.>12
    
 
    
    
        