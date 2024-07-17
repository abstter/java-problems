# This function generates a recipe for a certain food

import random

def template_to_recipe(ingredients):
    # Choose random recipe template
    recipe_templates = [
    
    '''Today's special is {ingredients[0][0]}{ingredients[0][1]} of {} mixed with,
    {}{} of {} and served with {}{} of
    {}.'''
        
    '''For a unique dish, combine {}{} of {} with
    {}{} of {}. Top it with {}{} of
    {}.'''
    ]
    
    template = random.choice(recipe_templates)
    print(template)
    # Fill in placeholders with info

def generate_recipe():
    ingredients = []
    
    for i in range(1, 4):
        ingredient = print(f"Enter the ingredient {i}: ")
        quantity = print(f"Enter the quantity {i}: ")
        unit = print(f"Enter the unit {i}: ")
        ingredients.append((quantity, unit, ingredient))
        
        recipe = template_to_recipe(ingredients)
        print("\nSilly Recipe!")
        print(recipe)
        
while True:
    generate_recipe()
    user_input = input("\nDo you want to generate another silly recipe.")
    if user_input != "yes":
        break
        
print("Goodbye!")

