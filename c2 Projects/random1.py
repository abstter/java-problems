# Abhiram Avasarala
import random
def num_guess():
    while True:
        num=str(random.choice(range(1,51)))
        answer=input("Choose number between 0 and 51. \n")
        if num==answer:
            print("Correct!")
            break
        else:
            print("Incorrect! it was",num,".")
            continue
num_guess()