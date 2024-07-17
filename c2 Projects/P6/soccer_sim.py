import time
import random

def soccer_sim():
    points = 0
    points1 = 0
    print("___________________________________________")
    print("Welcome to Soccer Simulator!!!!!!")
    time.sleep(1)
    print("This is my personal favorite game as I love the game of soccer!")
    time.sleep(2)
    print("In this game, you will get to choose where you want to shoot the soccer ball.")
    time.sleep(1)
    print("You will participate in the World Cup and see if you win and claim the title!!!")
    time.sleep(2)
    world_cup = ["France", "Germany", "Spain", "Portugal", "Australia", "America", "Belgium", "Argentina", "Brazil", "Mexico"]
    print("Selecting a team for you....")
    time.sleep(3)
    team = random.choice(world_cup)
    print("Your team is.....",team)
    time.sleep(2)
    goalkeepers = ["Peru", "Austria", "Germany", "England", "Norway", "America", "South Africa", "Morocco", "Saudia Arabia"]
    one = random.choice(goalkeepers)
    print("The goalkeeper you will be against is from........",one)
    time.sleep(1)
    print("Let the shoot-out commence!!!!!!!!!!")
    time.sleep(3)
    spot = input("Choose where you want to shoot the ball(make sure you type the word how it is shown): left top corner, right top corner, left bottom corner, right bottom corner, or center: ")
    time.sleep(2)
    goaliespot = ["left top corner", "right top corner", "left bottom corner", "right bottom corner", "center"]
    spot1 = random.choice(goaliespot)
    print("The goalkeeper dives to the",spot1,"!!!")
    if spot1 != spot:
        print("Good job, you scored!!")
        time.sleep(2)
        points = points + 1
        print("You have ",points,"points.")
    if spot1 == spot:
        print("Ah man, the goalie saved it. Better luck next time.")
        time.sleep(2)
        points = points
        print("You have ",points,"points.")
            
        
    print("The other team takes a shot........ and scores!!!")
    points1 = points1 + 1
    print("They have ",points1,"points.")
    time.sleep(1)
    print("Get ready for your 2nd shot......")
    time.sleep(1)
    spot = input("Choose where you want to shoot the ball(make sure you type the word how it is shown): left top corner, right top corner, left bottom corner, right bottom corner, or center: ")
    time.sleep(2)
    goaliespot = ["left top corner", "right top corner", "left bottom corner", "right bottom corner", "center"]
    spot1 = random.choice(goaliespot)
    print("The goalkeeper dives to the",spot1,"!!!")
    if spot1 != spot:
        print("Good job, you scored!!")
        time.sleep(2)
        points = points + 1
        print("You have ",points,"points.")
    if spot1 == spot:
        print("Ah man, the goalie saved it. Better luck next time.")
        time.sleep(2)
        points = points
        print("You have ",points,"points.")
    
    print("The other team takes a shot........ and miss!!!. What a save from your goalkeeper!")
    points1 = points1
    print("They have ",points1,"points.")
    print("Third shot comin up.....")
    time.sleep(1)
    spot = input("Choose where you want to shoot the ball(make sure you type the word how it is shown): left top corner, right top corner, left bottom corner, right bottom corner, or center: ")
    time.sleep(2)
    goaliespot = ["left top corner", "right top corner", "left bottom corner", "right bottom corner", "center"]
    spot1 = random.choice(goaliespot)
    print("The goalkeeper dives to the",spot1,"!!!")
    if spot1 != spot:
        print("Good job, you scored!!")
        time.sleep(2)
        points = points + 1
        print("You have ",points,"points.")
    if spot1 == spot:
        print("Ah man, the goalie saved it. Better luck next time.")
        time.sleep(2)
        points = points
        print("You have ",points,"points.")
        
    print("The other team takes a shot........ and score!!!. What a banger!")
    points1 = points1 + 1
    print("They have ",points,"points.")
    print("4th shot incoming......")
    time.sleep(1)
    spot = input("Choose where you want to shoot the ball(make sure you type the word how it is shown): left top corner, right top corner, left bottom corner, right bottom corner, or center: ")
    time.sleep(2)
    goaliespot = ["left top corner", "right top corner", "left bottom corner", "right bottom corner", "center"]
    spot1 = random.choice(goaliespot)
    print("The goalkeeper dives to the",spot1,"!!!")
    if spot1 != spot:
        print("Good job, you scored!!")
        time.sleep(2)
        points = points + 1
        print("You have ",points,"points.")
    if spot1 == spot:
        print("Ah man, the goalie saved it. Better luck next time.")
        time.sleep(2)
        points = points
        print("You have ",points,"points.")
        
    print("The other team takes their final shot....... and miss!!!")
    points1 = points1
    print("They have ",points1,"points.")
    if points > points1:
        print("You win!!!! ",points,"-",points1)
        time.sleep(1)
        print("Well done! You have beat the other team and claimed the title!!!")
    if points == points1:
        print("You tied. But, you are out of the World Cup. TOO BAD!!!")
    else:
        print("You lost!! Too bad. You're out!!!")
        
            

soccer_sim()