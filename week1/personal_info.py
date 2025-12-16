"""
TRISHA DABRAL
PROJECT DESCRIPTION:This project is a simple Python program that manages and displays personal
information. It combines static data (like your name and age) with dynamic input from the user 
(like favorite food and color). The goal is to practice variables, input handling, formatted 
output, and basic enhancements.
"""
print("="*48)
print("WELCOME TO YOUR PERSONAL INFORMATION MANAGER")
print("="*48)
#name-> Stores a string value "Trisha", representing the person’s name.
name="Trisha"
#age-> Stores an integer value 18, representing the person’s age.
age=18
#city-> Store a string value "Delhi", representing the city where person live.
city="Delhi"
#hobby->Store a string value "Dancing", representing hobby of the person
hobby="Dancing"
print("-"*48)
print("ANSWER THE FOLLOWING QUESTION")
print("-"*48)
fav_food=input("ENTER THE NAME OF YOUR FAVOURITE FOOD : ")
while(fav_food==""):
    print("INVAILD INPUT")
    fav_food=input("ENTER THE NAME OF YOUR FAVOURITE FOOD : ")
    fav_food=input("ENTER THE NAME OF YOUR FAVOURITE FOOD : ")
fav_color=input("ENTER THE NAME OF YOUR FAVOURITE COLOR : ")
while(fav_color==""):
    print("INVAILD INPUT")
    fav_food=input("ENTER THE NAME OF YOUR FAVOURITE COLOR : ")
print("="*48)
print("DISPLAYING YOUR INFORMATION")
print("="*48)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print("------------------------------")
print(f"Favorite Food: {fav_food}")
print(f"Favorite Color: {fav_color}")
print("------------------------------")
print(f"Age in months: {age * 12}")
print("="*48)
print("THANK YOU FOR USING THIS PROGRAM")
print("="*48)