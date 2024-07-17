"""
Project 4: Zoo Simulator
Student Code: Base Project
Python Level 3

Student Name: Abhiram A
Section: 8B-D14

For the base version of the Zoo Simulator program, implement the
following required features:

    1. a display_hierarchy() static method in the Animal class to 
       display the animal class hierarchy using a tree diagram
    2. a make_sound() method for each animal subclass to output a
       description of the sound the animal makes
    3. a weight attribute in the Animal class; the base_description()
       method should include the animal's weight in the output
    4. a Snake class that inherits from the Reptile class with the
       relevant methods overridden
    5. a feed_animals() method in the Habitat class that calls each
       animal's feed() method to make each animal eat

To see how the base project should work, run the Python script in

    MS3_P4_Zoo Simulator_Base Project_Solutions_ob.py
    
To get some enhancement ideas, see the project sheet and run the
Python script in

    MS3_P4_Zoo Simulator_Enhanced_Solutions_ob.py

"""

import random

class Animal:
    # parent class of all other animal classes
    population = 0
    
    def __init__(self, name, age, weight, habitat = None):
        # Each animal has a name, age, and possibly a habitat
        # (habitat is an optional parameter):
        self.name = name
        self.age = age
        self.habitat = habitat
        
        # Base Project Requirement #3:
        # ----------------------------
        self.weight = weight
        
        
    def make_sound(self):
        pass

    def feed(self):
        pass

    def play(self):
        pass

    def sleep(self):
        pass
    
    def base_description(self):
        # All animals have the name and age attributes, so
        # these are part of the basic animal description.
        
        # Base Project Requirement #3:
        # ----------------------------
        # Include the new weight attribute in the description:
        print(f"{self.name} is {self.age} years old and weighs {self.weight} pounds.")
        
    def description(self):
        # This will be a more specialized method defined in each
        # subclass to describe instance attributes unique to it.        
        pass
        
    def compare_weights(self, other_weight, label):
        # Enhancement #1:
        # The compare_weights() method should calculate the weight
        # difference between the animal's weight and other_weight. 
        # It should report whether the animal's weight is less than, 
        # greater than, or equal to other_weight and display the
        # difference, if any.
        #
        # The label parameter contains a string identifying what
        # other_weight represents, so use it in this method's output
        # message to identify the comparison being done (e.g. label 
        # could mark other_weight as a habitat average, a class
        # average, or something else).
        pass
    
    @classmethod
    def increment_pop(cls):
        cls.population += 1
        
    @classmethod
    def decrement_pop(cls):
        cls.population -= 1

    @classmethod
    def get_pop(cls):
        animal_population = 0
        subclasses = Animal.__subclasses__()
        for subclass in subclasses:
            animal_population += subclass.get_pop()
        return animal_population
    
    @staticmethod
    def display_hierarchy():
        # Base Project Requirement #1:
        # Adds print statements which create a animal class hierarchy
        print("Animal Class Hierarchy")
        print("-------------------------")
        print("Animal")
        print("|---- Mammal")
        print("|        |----Koala")
        print("|        |----Llama")
        print("|       |----Lion")
        print("|")
        print("|---- Reptile")
        print("|        |----Snake")
  

class Mammal(Animal):
    warm_blooded = True
    
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
    
    @classmethod
    def get_pop(cls):
        mammal_population = 0
        subclasses = Mammal.__subclasses__()
        for subclass in subclasses:
            mammal_population += subclass.get_pop()
        return mammal_population
        

class Koala(Mammal):
    population = 0
    
    def __init__(self, name, age, weight, favorite_tree):
        super().__init__(name + " the Koala", age, weight)
        self.favorite_tree = favorite_tree
        Koala.increment_pop()

    def make_sound(self):
        # Base Project Requirement #2
        # Print out the koala sound using self.name
        print(f"{self.name} is grunting very LOUDLY.")
        pass

    def feed(self):
        print(f"{self.name} is munching on some",
              f"{self.favorite_tree} eucalyptus leaves!")

    def play(self):
        playmate = random.choice(list(self.habitat.animals.keys()))
        print(f"{self.name} is climbing trees and playing",
              f"with {playmate}.")

    def sleep(self):
        print(f"{self.name} is taking a nap in a",
              f"{self.favorite_tree} tree.")
        
    def description(self):
        self.base_description()
        print(f"Its favorite eucalyptus tree is {self.favorite_tree}.")

    @classmethod
    def get_pop(cls):
        return cls.population


class Lion(Mammal):
    population = 0
    
    def __init__(self, name, age, weight, mane_color):
        super().__init__(name + " the Lion", age, weight)
        self.mane_color = mane_color
        Lion.increment_pop()

    def make_sound(self):
        # Base Project Requirement #2
        # ----------------------------
        # Implement the make_sound() method for animal subclasses.
        # if statement that says if the lion has a mane color then it shakes it and if it doesnt
        # then it just roars proudly
        if mane_color == 'none':
            print(f"{self.name} roars proudly!")
        else:
            print(f"{self.name} shakes out its {self.mane_color} glamorously and roars!")

    def feed(self):
        print(f"{self.name} is feasting on some meat.")

    def play(self):
        playmate = random.choice(list(self.habitat.animals.keys()))
        if playmate == self.name:
            print(f"{self.name} is playfully chasing its own tail.")
        else:
            print(f"{self.name} is playfully chasing {playmate}.")

    def sleep(self):
        print(f"{self.name} is snoozing under a tree.")
    
    def description(self):
        self.base_description()
        if self.mane_color == "none":
            print("It has no mane.")
        else:
            print(f"Its mane is {self.mane_color} in color.")

    @classmethod
    def get_pop(cls):
        return cls.population


class Llama(Mammal):
    population = 0
    
    def __init__(self, name, age, weight, wool_color):
        super().__init__(name + " the Llama", age, weight)
        self.wool_color = wool_color
        Llama.increment_pop()

    def make_sound(self):
        # Base Project Requirement #2
        # Print out the llama sound using self.name
        print(f"{self.name} is braying LOUDLY.")
        pass

    def feed(self):
        print(f"{self.name} is eating some hay.")

    def play(self):
        playmate = random.choice(list(self.habitat.animals.keys()))
        if playmate == self.name:
            print(f"{self.name} is frolicking by itself.")
        else:
            print(f"{self.name} is frolicking with {playmate}.")

    def sleep(self):
        print(f"{self.name} is lying down for a rest.")
    
    def description(self):
        self.base_description()
        print(f"Its wool is {self.wool_color} in color.")

    @classmethod
    def get_pop(cls):
        return cls.population
    

class Reptile(Animal):
    warm_blooded = False
    
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
    
    @classmethod
    def get_pop(cls):
        reptile_population = 0
        subclasses = Reptile.__subclasses__()
        for subclass in subclasses:
            reptile_population += subclass.get_pop()
        return reptile_population


# Base Project Requirement #4
# ----------------------------
# Create the Snake class, inheriting from the Reptile class.
# Wherever appropriate, override methods inherited from Snake's
# parent classes (which includes Animal). See the sample program
# for output: MS3_P3_Zoo Simulator_Base Project Sample_ob.py
class Snake(Reptile):
    population = 0
    
    def __init__(self, name, age, weight, scale_color):
        super().__init__(name + " the Snake", age, weight)
        self.scale_color = scale_color
        Snake.increment_pop()

    def make_sound(self):
        # Base Project Requirement #2
        # Print the snake sound using self.name
        print(f"{self.name} is hissing LOUDLY to scare off the other animals.")
        pass

    def feed(self):
        # Print how the snake is eating and what it is eating
        print(f"{self.name} is eating mice and rabbits happily.")

    def play(self):
        # Print that if the snake is by itself, it buried in the ground and if it is with another,
        # then it is slithering
        playmate = random.choice(list(self.habitat.animals.keys()))
        if playmate == self.name:
            print(f"{self.name} is buried in the ground by itself.")
        else:
            print(f"{self.name} is slithering with another {playmate}.")

    def sleep(self):
        # How the snake sleeps
        print(f"{self.name} coils up for a peaceful sleep.")
    
    def description(self):
        # Color of the snake scales
        self.base_description()
        print(f"Its scale is {self.scale_color} in scale.")
    
    @classmethod
    def get_pop(cls):
        return cls.population


class Habitat:
    def __init__(self, habitat_type):
        self.habitat_type = habitat_type
        self.animals = {}
    
    def add_animal(self, animal):
        if animal.name in self.animals:
            print("An animal with this name already exists in",
                  f"{self.habitat_type}.")
            return

        self.animals[animal.name] = animal
        animal.habitat = self
        print(f"{animal.name} has been added to the",
              f"{self.habitat_type} habitat.")

    def remove_animal(self, name):
        if name not in self.animals:
            print("No animal with this name exists in the habitat.")
            return
        
        type(self.animals[name]).decrement_pop()
        del self.animals[name]
        print(f"{name} has been removed from the",
              f"{self.habitat_type} habitat.")

    def feed_animals(self):
        # Base Project Requirement #5:
        # ----------------------------
        # Implement the feed_animals() method, which will loop
        # through all animals in the habitat and call the feed()
        # method of each animal:
        # for loop that says when the animals are in the value of animals, then the feed method is used
        print(f"\nThe animals in the {self.habitat_type}",
              "begin eating...\n")
        for animals in self.animals.values():
            animals.feed()
        

    def play_with_animals(self):
        print(f"\nThe animals in the {self.habitat_type}",
              "begin playing...\n")
        for animal in self.animals.values():
            animal.play()

    def let_animals_sleep(self):
        print(f"\nThe animals in the {self.habitat_type}",
              "begin sleeping...\n")
        for animal in self.animals.values():
            animal.sleep()

    def simulate_day(self):
        # Enhancement #3:
        # ---------------
        # Implement the Habitat simulate_day() method. It should
        # traverse the habitat's animals and randomly run the feed(),
        # play(), or sleep() method of each animal, simulating a
        # random selection of a day’s activities.
        pass
            
    def get_pop(self):
        # Return the size of the animal population in the habitat.
        return len(self.animals)
    
    def compare_weights(self):
        # Gets the average weight of all animals in the habitat and
        # compares each animal's weight to that average.
        
        total_weight = 0
        animal_count = 0

        for animal in self.animals.values():
            # Sum up the weights of all the animals in habitat
            total_weight += animal.weight
            animal_count += 1
        
        # Calculate the average weight, defaulting to 0 if habitat
        # has no animals to avoid division-by-0 error:
        avg_weight = total_weight / animal_count \
                         if animal_count > 0 else 0
        avg_weight = round(avg_weight, 2)

        for animal in self.animals.values():
            # Iterate over the habitat's animal objects to compare 
            # each animal's weight to the average of the habitat.
            # Label the input weight as the "habitat average".
            animal.compare_weights(avg_weight, "habitat average")
     
     
class Zoo:
    def __init__(self):
        self.habitats = {}

    def add_habitat(self, habitat_type):
        if habitat_type not in self.habitats:
            self.habitats[habitat_type] = Habitat(habitat_type)
            print(f"{habitat_type} habitat has been added.")
        else:
            print(f"{habitat_type} habitat already exists.")

    def remove_habitat(self, habitat_type):
        if habitat_type in self.habitats:
            del self.habitats[habitat_type]
            print(f"{habitat_type} habitat has been removed.")
        else:
            print(f"{habitat_type} habitat does not exist.")

    def simulate_day(self):
        for habitat in self.habitats.values():
            habitat.simulate_day()
            
    def display_habitats(self, detailed = False):
        # Enhancement #2:
        # ---------------
        # In the Zoo class, modify the display_habitats() method to
        # accept an optional detailed parameter (it should be False
        # by default).
        #
        # If detailed is set to True, the method should also
        # display a description of each animal in the habitat by
        #    calling the animal’s description() method.

        print('\nListing habitats and animals:')
        
        if not self.habitats:
            print("\nNo habitats in the zoo.")
        for habitat in self.habitats.values():
            print(f"\n{habitat.habitat_type} habitat:")
            if not habitat.animals:
                print("  No animals in this habitat.")
            else:
                for animal in habitat.animals.values():
                    print(f"  {animal.name}")
                    if detailed:
                        print('    ', end = '')
                        animal.description()
    
    def get_habitat_choice(self, purpose = "for your action"):
        if not self.habitats:
            print("\nNo habitats in the zoo.")
            return False
        print("Select a habitat", purpose + ":")
        i = 1
        for habitat in self.habitats.keys():
            print(f"{i}. {habitat}")
            i += 1
        # Alternate for loop using enumerate():
        # for i, habitat in enumerate(self.habitats.keys(), 1):
        #        print(f"{i}. {habitat}")
        
        while True:
            habitat_i = int(input("Enter the habitat number: ")) - 1
            if habitat_i < 0 or habitat_i >= len(self.habitats):
                print("Invalid habitat number.")
                continue
            break
        habitat_type = list(self.habitats.keys())[habitat_i]
        return habitat_type

    def population_audit(self):
        # Enhancement #4:
        # ---------------
        # Implement the population_audit() method, which displays
        # various population statistics for the zoo, habitats, and
        # animal classes and checks whether the population counts
        # are accurate (as a way of checking that the system works
        # and that population data has been updated correctly).
        # This accuracy should be based on whether different
        # population totals are consistent with each other.
        #
        # See the obfuscated Enhanced Solution for output details:
        # MS3_P3_Zoo Simulator_Enhanced Solution_ob.py
        
        print('\nConducting a zoo population audit...')

    def compare_weights(self):
        for habitat in self.habitats.values():
            print(f"\n{habitat.habitat_type} weight comparisons:")
            habitat.compare_weights()
  
  
def populate(zoo):
    zoo.add_habitat('African Savannah')
    zoo.add_habitat('Andean Meadow')
    zoo.add_habitat('Eucalyptus Forest')
    zoo.add_habitat('Rainforest')
    
    savannah_hab = zoo.habitats['African Savannah']
    meadow_hab = zoo.habitats['Andean Meadow']
    euc_forest_hab = zoo.habitats['Eucalyptus Forest']
    rainforest_hab = zoo.habitats['Rainforest']
    
    euc_forest_hab.add_animal(Koala('Suzy', 2, 16, 'Scribbly Gum'))
    euc_forest_hab.add_animal(Koala('Bob', 4, 21, 'Blue Gum'))
    euc_forest_hab.add_animal(Koala('Kai', 3, 19, 'Red Mahogany'))
    
    savannah_hab.add_animal(Lion('Leo', 7, 445, 'tawny'))
    savannah_hab.add_animal(Lion('Kate', 4, 330, 'none'))
    savannah_hab.add_animal(Koala('Jon', 4, 18, 'White Ash'))
    savannah_hab.add_animal(Llama('Finn', 6, 350, 'cream'))
    
    meadow_hab.add_animal(Llama('Bart', 5, 335, 'red'))
    meadow_hab.add_animal(Llama('Jin', 3, 265, 'fawn and honey'))
    
    # Base Project Requirement #4
    # ---------------------------
    # Uncomment the three lines of code below to populate the
    # rainforest habitat with snakes, testing your Snake class:
    
    rainforest_hab.add_animal(Snake('Naga', 5, 5, 'black and yellow bands'))
    rainforest_hab.add_animal(Snake('Kaa', 7, 6, 'brown and tan diamonds'))
    rainforest_hab.add_animal(Snake('Vip', 3, 4, 'green with white zigzags'))
    
    
def main():
    print("Welcome to the Zoo Simulator!\n")
    
    zoo = Zoo()
    populate(zoo)
        
    while True:
        print('\n*****************')
        print('* Zoo Main Menu *')
        print('*****************')
        print("Available actions:")
        print("1. Display habitats")
        print("2. Display detailed habitats")
        print("3. Display the animal class hierarchy")
        print("4. Conduct a population audit")
        print("5. Add habitat")
        print("6. Remove habitat")
        print("7. Add animal")
        print("8. Remove animal")
        print("9. Feed animals")
        print("10. Play with animals")
        print("11. Let animals sleep")
        print("12. Simulate a day in the zoo")
        print("13. Compare animal weights")
        print("0. Exit")

        action = input("\nEnter your choice: ")
        
        if action == "0":
            break
        
        elif action == "1":
            zoo.display_habitats()
            
        elif action == "2":
            # Enhancement #2:
            # ---------------
            # Modify this option in the main() menu to call
            # display_habitats() with detailed equal to True
            # to display the habitats and animals in detail:
            zoo.display_habitats(detailed = True)
            
        elif action == "3":
            Animal.display_hierarchy()
        
        elif action == "4":
            zoo.population_audit()
            
        elif action == "5":
            habitat_type = input("Enter the habitat type: ")
            zoo.add_habitat(habitat_type)
            
        elif action == "6":
            habitat_type = zoo.get_habitat_choice("to remove")
            if not habitat_type:
                continue
            zoo.remove_habitat(habitat_type)
            
        elif action == "7":
            habitat_type = zoo.get_habitat_choice("to add an animal to")
            if not habitat_type:
                continue
            hab = zoo.habitats[habitat_type]
            
            if hab.animals:
                print('Existing animals include:')
                for i, animal in enumerate(hab.animals.values(), 1):
                    print(i, end = ': ')
                    animal.description()
                    
            animal_type = input("Enter the animal type to add: ").lower()
            if not animal_type in ["koala", "lion", "llama", "snake"]:
                print("Invalid animal type.")
                continue
            
            name = input("Enter the animal's name: ")
            age = int(input("Enter the animal's age (integer): "))
            weight = int(input("Enter the animal's weight in lbs"
                               + "(integer): "))
            if animal_type == "koala":
                favorite_tree = input("Enter the koala's favorite tree: ")
                animal = Koala(name, age, weight, favorite_tree)
            elif animal_type == "lion":
                mane_color = input("Enter the lion's mane color: ")
                animal = Lion(name, age, weight, mane_color)
            elif animal_type == "llama":
                wool_color = input("Enter the llama's wool color: ")
                animal = Llama(name, age, weight, wool_color)
            elif animal_type == "snake":
                pattern = input("Enter the snake's scale pattern: ")
                animal = Snake(name, age, weight, pattern)         
            
            hab.add_animal(animal)
            
        elif action == "8":
            habitat_type = zoo.get_habitat_choice("to remove an animal from")
            if not habitat_type:
                continue
            hab = zoo.habitats[habitat_type]
            
            if hab.animals:
                print('Existing animals include:')
                for i, animal in enumerate(hab.animals.keys()):
                    print(i, ':', animal)
                    
            name = input("Enter the animal's name: ")
            hab.remove_animal(name)
            
        elif action == "9":
            habitat_type = zoo.get_habitat_choice("whose animals to feed")
            if not habitat_type:
                continue
            zoo.habitats[habitat_type].feed_animals()
                
        elif action == "10":
            habitat_type = zoo.get_habitat_choice("for the play action")
            if not habitat_type:
                continue
            zoo.habitats[habitat_type].play_with_animals()
            
        elif action == "11":
            habitat_type = zoo.get_habitat_choice("for the sleep action")
            if not habitat_type:
                continue
            zoo.habitats[habitat_type].let_animals_sleep()
            
        elif action == "12":
            zoo.simulate_day()
        
        elif action == "13":
            zoo.compare_weights()
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

'''
*****************
* Zoo Main Menu *
*****************
Available actions:
1. Display habitats
2. Display detailed habitats
3. Display the animal class hierarchy
4. Conduct a population audit
5. Add habitat
6. Remove habitat
7. Add animal
8. Remove animal
9. Feed animals
10. Play with animals
11. Let animals sleep
12. Simulate a day in the zoo
13. Compare animal weights
0. Exit

Enter your choice: 1

Listing habitats and animals:

African Savannah habitat:
  Leo the Lion
  Kate the Lion
  Jon the Koala
  Finn the Llama

Andean Meadow habitat:
  Bart the Llama
  Jin the Llama

Eucalyptus Forest habitat:
  Suzy the Koala
  Bob the Koala
  Kai the Koala

Rainforest habitat:
  Naga the Snake
  Kaa the Snake
  Vip the Snake

*****************
* Zoo Main Menu *
*****************
Available actions:
1. Display habitats
2. Display detailed habitats
3. Display the animal class hierarchy
4. Conduct a population audit
5. Add habitat
6. Remove habitat
7. Add animal
8. Remove animal
9. Feed animals
10. Play with animals
11. Let animals sleep
12. Simulate a day in the zoo
13. Compare animal weights
0. Exit

Enter your choice: 2

Listing habitats and animals:

African Savannah habitat:
  Leo the Lion
    Leo the Lion is 7 years old and weighs 445 pounds.
Its mane is tawny in color.
  Kate the Lion
    Kate the Lion is 4 years old and weighs 330 pounds.
It has no mane.
  Jon the Koala
    Jon the Koala is 4 years old and weighs 18 pounds.
Its favorite eucalyptus tree is White Ash.
  Finn the Llama
    Finn the Llama is 6 years old and weighs 350 pounds.
Its wool is cream in color.

Andean Meadow habitat:
  Bart the Llama
    Bart the Llama is 5 years old and weighs 335 pounds.
Its wool is red in color.
  Jin the Llama
    Jin the Llama is 3 years old and weighs 265 pounds.
Its wool is fawn and honey in color.

Eucalyptus Forest habitat:
  Suzy the Koala
    Suzy the Koala is 2 years old and weighs 16 pounds.
Its favorite eucalyptus tree is Scribbly Gum.
  Bob the Koala
    Bob the Koala is 4 years old and weighs 21 pounds.
Its favorite eucalyptus tree is Blue Gum.
  Kai the Koala
    Kai the Koala is 3 years old and weighs 19 pounds.
Its favorite eucalyptus tree is Red Mahogany.

Rainforest habitat:
  Naga the Snake
    Naga the Snake is 5 years old and weighs 5 pounds.
Its scale is black and yellow bands in scale.
  Kaa the Snake
    Kaa the Snake is 7 years old and weighs 6 pounds.
Its scale is brown and tan diamonds in scale.
  Vip the Snake
    Vip the Snake is 3 years old and weighs 4 pounds.
Its scale is green with white zigzags in scale.

*****************
* Zoo Main Menu *
*****************
Available actions:
1. Display habitats
2. Display detailed habitats
3. Display the animal class hierarchy
4. Conduct a population audit
5. Add habitat
6. Remove habitat
7. Add animal
8. Remove animal
9. Feed animals
10. Play with animals
11. Let animals sleep
12. Simulate a day in the zoo
13. Compare animal weights
0. Exit

Enter your choice: 3
Animal Class Hierarchy
-------------------------
Animal
|---- Mammal
|        |----Koala
|        |----Llama
|       |----Lion
|
|---- Reptile
|        |----Snake

*****************
* Zoo Main Menu *
*****************
Available actions:
1. Display habitats
2. Display detailed habitats
3. Display the animal class hierarchy
4. Conduct a population audit
5. Add habitat
6. Remove habitat
7. Add animal
8. Remove animal
9. Feed animals
10. Play with animals
11. Let animals sleep
12. Simulate a day in the zoo
13. Compare animal weights
0. Exit

Enter your choice: 9
Select a habitat whose animals to feed:
1. African Savannah
2. Andean Meadow
3. Eucalyptus Forest
4. Rainforest
Enter the habitat number: 4

The animals in the Rainforest begin eating...

Naga the Snake is eating mice and rabbits happily.
Kaa the Snake is eating mice and rabbits happily.
Vip the Snake is eating mice and rabbits happily.
'''