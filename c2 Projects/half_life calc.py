# Abhiram Avasarala Project 3

import math
import time,re
alife=0
ahlife=0
def half_life_calc():
    print("------------------Half Life Calculator-----------")
    time.sleep(0.5)
    print("Enter all values without units.")
    time.sleep(0.5)
    print("You will be prompted for units separately.")
    name=input("What is the name of the substance?\n")
    time.sleep(0.5)
    mass=float(input("What is the initial mass of the substance?\n"))
    time.sleep(0.5)
    temass=float(input("What is the target ending mass of the substance?\n"))
    time.sleep(0.5)
    umass=input("What is the unit of the mass?\n")
    time.sleep(0.5)
    hlife=float(input("What is the half-life of the substance?\n"))
    time.sleep(0.5)
    utime=input("What is the unit of time?\n")
    time.sleep(0.5)
    print("Half-Life Table for",name+":",mass,umass,"to",temass,umass+".")
    print("___________________________________________________________________")
    print("Half-Lives Elapsed        Time Elapsed in",utime,"        ",name,"Amount",umass)
    print("__________________________________________________________________________________")
    while mass>temass:
        global alife
        global ahlife
        print(str(alife).ljust(22, " "),str(ahlife).ljust(25," "),mass)
        time.sleep(0.5)
        mass=mass/2
        alife=alife+1
        ahlife=alife*hlife
        ahlife=str(ahlife)
    print(str(alife).ljust(22, " "),str(ahlife).ljust(25," "),mass)
    time.sleep(0.5)
    mass=mass/2
    alife=alife+1
    ahlife=alife*hlife
    ahlife=str(ahlife)
    print("\n\n\n")
    

def time_dilation_calc():
    print("Time Dilation Calculator")
    print("________________________________________________________________________")
    print("Enter all the numbers without their units; units will be prompted separately.")
    t=input("Enter the length of the universal travel time:\n")
    u=input("Enter the unit of the time:\n")
    print("Time Dilation Table\n_______________________________________________")
    print("Percent of Light Speed               Travel Time                   Time Dilation              Earth Time")
    print("=================================================================================================================")
    a=0
    while a < 100:
        if a<81:
            if a%10==0:
                time.sleep(0.03)
                to=float(t)/(math.sqrt(1-((a/100)**2)))
                c=to/float(t)
                print("      ", a,  "%  light speed  \t\t\t\t      ", float(t), u.ljust(8," "),  "      x", str(round(c,2)).ljust(10, " "),"      ", round(float(t)*c, 2), u)
            a += 1
        else:
            time.sleep(0.03)
            to=float(t)/(math.sqrt(1-((a/100)**2)))
            c=to/float(t)
            print("      ", a,  "%  light speed  \t\t\t\t      ", float(t), u.ljust(8," "),  "      x", str(round(c,2)).ljust(10, " "),"      ", round(float(t)*c, 2), u)
            a+=1


def menu():
    print("\n\n\n")
    print("Welcome to Abhiram Avasarala's project 3!")
    time.sleep(1)
    print("What program do you want to run?")
    print("         1. HALF LIFE CALCULATOR")
    print("         2. TIME DILATION CALCULATOR")
    print("         3. EXIT")
    choice = input("")
    if choice == "1":
        half_life_calc()
    elif choice == "2":
        time_dilation_calc()
    elif choice == "3":
        exit()
    else:
        menu()
menu()
# Output Files
# Half-Life Calculator
"""
------------------Half Life Calculator-----------
What is the name of the substance?
Coffee
What is the initial mass of the substance?
100
What is the target ending mass of the substance?
0.1
What is the unit of the mass?
mg
What is the half-life of the substance?
5.5
What is the unit of time?
hours
Half-Life Table for Coffee: 100.0 mg to 0.1 mg.
___________________________________________________________________
Half-Lives Elapsed        Time Elapsed in hours          Coffee Amount mg
__________________________________________________________________________________
0                      0                         100.0
1                      5.5                       50.0
2                      11.0                      25.0
3                      16.5                      12.5
4                      22.0                      6.25
5                      27.5                      3.125
6                      33.0                      1.5625
7                      38.5                      0.78125
8                      44.0                      0.390625
9                      49.5                      0.1953125
10                     55.0                      0.09765625

"""

"""
------------------Half Life Calculator-----------
Enter all values without units.
You will be prompted for units separately.
What is the name of the substance?
Alcohol
What is the initial mass of the substance?
84
What is the target ending mass of the substance?
0.1
What is the unit of the mass?
g
What is the half-life of the substance?
2
What is the unit of time?
hours
Half-Life Table for Alcohol: 84.0 g to 0.1 g.
___________________________________________________________________
Half-Lives Elapsed        Time Elapsed in hours          Alcohol Amount g
__________________________________________________________________________________
0                      0                         84.0
1                      2.0                       42.0
2                      4.0                       21.0
3                      6.0                       10.5
4                      8.0                       5.25
5                      10.0                      2.625
6                      12.0                      1.3125
7                      14.0                      0.65625
8                      16.0                      0.328125
9                      18.0                      0.1640625
10                     20.0                      0.08203125

"""

"""
------------------Half Life Calculator-----------
Enter all values without units.
You will be prompted for units separately.
What is the name of the substance?
Plutonium-239
What is the initial mass of the substance?
10
What is the target ending mass of the substance?
2
What is the unit of the mass?
kg
What is the half-life of the substance?
24000
What is the unit of time?
years
Half-Life Table for Plutonium-239: 10.0 kg to 2.0 kg.
___________________________________________________________________
Half-Lives Elapsed        Time Elapsed in years          Plutonium-239 Amount kg
__________________________________________________________________________________
0                      0                         10.0
1                      24000.0                   5.0
2                      48000.0                   2.5
3                      72000.0                   1.25

"""

"""
------------------Half Life Calculator-----------
Enter all values without units.
You will be prompted for units separately.
What is the name of the substance?
Nihonium-284
What is the initial mass of the substance?
10
What is the target ending mass of the substance?
2
What is the unit of the mass?
kg
What is the half-life of the substance?
0.48
What is the unit of time?
seconds
Half-Life Table for Nihonium-284: 10.0 kg to 2.0 kg.
___________________________________________________________________
Half-Lives Elapsed        Time Elapsed in seconds          Nihonium-284 Amount kg
__________________________________________________________________________________
0                      0                         10.0
1                      0.48                      5.0
2                      0.96                      2.5
3                      1.44                      1.25
"""

"""
Time Dilation Calculator
________________________________________________________________________
Enter all the numbers without their units; units will be prompted separately.
Enter the length of the universal travel time:
180
Enter the unit of the time:
days
Time Dilation Table
_______________________________________________
Percent of Light Speed               Travel Time                   Time Dilation              Earth Time
=================================================================================================================
       0 %  light speed  				       180.0 days           x 1.0               180.0 days
       10 %  light speed  				       180.0 days           x 1.01              180.91 days
       20 %  light speed  				       180.0 days           x 1.02              183.71 days
       30 %  light speed  				       180.0 days           x 1.05              188.69 days
       40 %  light speed  				       180.0 days           x 1.09              196.4 days
       50 %  light speed  				       180.0 days           x 1.15              207.85 days
       60 %  light speed  				       180.0 days           x 1.25              225.0 days
       70 %  light speed  				       180.0 days           x 1.4               252.05 days
       80 %  light speed  				       180.0 days           x 1.67              300.0 days
       81 %  light speed  				       180.0 days           x 1.71              306.94 days
       82 %  light speed  				       180.0 days           x 1.75              314.49 days
       83 %  light speed  				       180.0 days           x 1.79              322.72 days
       84 %  light speed  				       180.0 days           x 1.84              331.74 days
       85 %  light speed  				       180.0 days           x 1.9               341.7 days
       86 %  light speed  				       180.0 days           x 1.96              352.74 days
       87 %  light speed  				       180.0 days           x 2.03              365.07 days
       88 %  light speed  				       180.0 days           x 2.11              378.97 days
       89 %  light speed  				       180.0 days           x 2.19              394.77 days
       90 %  light speed  				       180.0 days           x 2.29              412.95 days
       91 %  light speed  				       180.0 days           x 2.41              434.14 days
       92 %  light speed  				       180.0 days           x 2.55              459.28 days
       93 %  light speed  				       180.0 days           x 2.72              489.72 days
       94 %  light speed  				       180.0 days           x 2.93              527.59 days
       95 %  light speed  				       180.0 days           x 3.2               576.46 days
       96 %  light speed  				       180.0 days           x 3.57              642.86 days
       97 %  light speed  				       180.0 days           x 4.11              740.42 days
       98 %  light speed  				       180.0 days           x 5.03              904.53 days
       99 %  light speed  				       180.0 days           x 7.09              1275.99 days

"""



"""
Time Dilation Calculator
________________________________________________________________________
Enter all the numbers without their units; units will be prompted separately.
Enter the length of the universal travel time:
30
Enter the unit of the time:
years
Time Dilation Table
_______________________________________________
Percent of Light Speed               Travel Time                   Time Dilation              Earth Time
=================================================================================================================
       0 %  light speed  				       30.0 years          x 1.0               30.0 years
       10 %  light speed  				       30.0 years          x 1.01              30.15 years
       20 %  light speed  				       30.0 years          x 1.02              30.62 years
       30 %  light speed  				       30.0 years          x 1.05              31.45 years
       40 %  light speed  				       30.0 years          x 1.09              32.73 years
       50 %  light speed  				       30.0 years          x 1.15              34.64 years
       60 %  light speed  				       30.0 years          x 1.25              37.5 years
       70 %  light speed  				       30.0 years          x 1.4               42.01 years
       80 %  light speed  				       30.0 years          x 1.67              50.0 years
       81 %  light speed  				       30.0 years          x 1.71              51.16 years
       82 %  light speed  				       30.0 years          x 1.75              52.41 years
       83 %  light speed  				       30.0 years          x 1.79              53.79 years
       84 %  light speed  				       30.0 years          x 1.84              55.29 years
       85 %  light speed  				       30.0 years          x 1.9               56.95 years
       86 %  light speed  				       30.0 years          x 1.96              58.79 years
       87 %  light speed  				       30.0 years          x 2.03              60.85 years
       88 %  light speed  				       30.0 years          x 2.11              63.16 years
       89 %  light speed  				       30.0 years          x 2.19              65.8 years
       90 %  light speed  				       30.0 years          x 2.29              68.82 years
       91 %  light speed  				       30.0 years          x 2.41              72.36 years
       92 %  light speed  				       30.0 years          x 2.55              76.55 years
       93 %  light speed  				       30.0 years          x 2.72              81.62 years
       94 %  light speed  				       30.0 years          x 2.93              87.93 years
       95 %  light speed  				       30.0 years          x 3.2               96.08 years
       96 %  light speed  				       30.0 years          x 3.57              107.14 years
       97 %  light speed  				       30.0 years          x 4.11              123.4 years
       98 %  light speed  				       30.0 years          x 5.03              150.76 years
       99 %  light speed  				       30.0 years          x 7.09              212.66 years

""" 