
"""
Exercise 8 with Optional Requirements
Simple Search
ASSESSMENT 1
"""

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]#list of names


search_name = input("Enter the name you want to search for: ")#variable used to ask for user input on which name to search for


if search_name in names:#search functionality used to check if the user input(search_name) is in the list (names)
    print(search_name, "was found in the list.")#if in the list then it prints that the user input was found in the list
else:#if not in the list else condition used
    print(search_name, "was not found in the list.")#shows that the user input is not in the list

