# This code generates a recipe for a certain food

def recipe_intro():
    print("Welcome to the Silly Recipe Builder!\n")
    print('''In this program, you will be asked to input three ingredients,
including their quantities and units. The program will then output
a silly recipe based on your inputs.\n''')
    print("Let's get started!\n")
    
recipe_intro()

def generate_recipe():
    my_list = []
    for i in range(3):
        name = input(f"Enter the name of ingredient 1: ")
        qty = float(input(f"Enter the quantity of {name} you want to use: "))
        unit = input("Enter the unit for that quantity (e.g. cups, grams): ")
        my_list.append[name, qty, unit]
        
        
                
    
generate_recipe()
    
    
    