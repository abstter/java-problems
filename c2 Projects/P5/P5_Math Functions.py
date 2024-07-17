# Abhiram Avasarala B1 Project 5
# January 24 2021
# 'The cookies were definitely stolen by the neighbors clever Eurasian magpie'



#1)
import math

def volume(r):
    # We need to calculate the sphere's volume so we can take the radius which is 'r' and use the formula to calculate it
    x=(4/3)*3.1415*r**3
    return round(x)
    
print(volume(10), "units")

#2)
import math

def temp(C):
    # The next two lines do the conversion, step by step
    F=(C*9/5) + 32
    return round(F,1)
print(temp(10), "degrees Fahrenheit")

#3)
import math

def height(f, i):
    # We need to convert both the feet and inch values to centimeters. Then we add them up.
    fc=f*12*2.54
    ic=i*2.54
    tc=fc+ic
    rtc=round(tc,0)
    k = print(rtc, 'centimeters')
    return tc

print(height(5,3), "centimeters")

#4)

def investement(s, x, y):
    # We plug our three variables into the formula
    ev=s*(1 +y/100)**x
    rev=round(ev, 0)
    return rev
print(investement(20000,30,5),"dollars")
 

# Outputs

#1. 33.51 units^3
#2. 50.0 degrees
#3. 160.0 centimeters
#4. $86439



    
    
    