import random

def template_to_recipe(ingredients):
    
    recip1 = f"Today's special is {ingredients[0][0]} {ingredients[0][1]} of {ingredients[0][2]}"\
+f"mixed with {ingredients[1][0]} {ingredients[1][1]} of {ingredients[1][2]}. Combine it with {ingredients[2][0]} {ingredients[2][1]} of"\
+f"{ingredients[2][2]}."
    
    recip2 = f"Mix {ingredients[0][0]} {ingredients[0][1]} of {ingredients[0][2]} with {ingredients[1][0]} {ingredients[1][1]} of"\
+f"{ingredients[1][2]}. Add {ingredients[2][0]} {ingredients[2][1]} of {ingredients[2][2]} to it."
    
    recip3 = f"Combine {ingredients[0][0]} {ingredients[0][1]} of {ingredients[0][2]} with {ingredients[1][0]} {ingredients[1][1]} of"\
+f"{ingredients[1][2]}. Spice it up with {ingredients[2][0]} {ingredients[2][1]} of {ingredients[2][2]}."
    
    recipe_templates = [recip1, recip2, recip3]
    template = random.choice(recipe_templates)
def generate_recipe():
    ingredients = []
    while True:
        for i in range(1, 4):
            ingredient = input(f"Enter the ingredient {i}: ")
            quantity = int(input(f"Enter the quantity {i}: "))
            unit = input(f"Enter the unit {i}: ")
            ingredients.append((quantity, unit, ingredient))
        
            recipe = template_to_recipe(ingredients)
            print("\nSilly Recipe!")
            print(recipe)

            user_input = input("\nDo you want to generate another silly recipe.")
            if user_input != "yes":
                break
            print("Goodbye!!")
        
generate_recipe()
        
        