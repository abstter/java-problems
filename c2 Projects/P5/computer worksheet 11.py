"Abhiram Avasarala B1 Worksheet 11 3/7/22"
import math
#1.
def circ_area(r):
    return math.pi*(r**2)
                    

def cyl_vol(r,h):
    return circ_area(r)*h
print(round(cyl_vol(10,1),2), "cu.m")


#2.
def is_odd(x):
    if x % 2==0:
        return("True")
    else: 
        return("False")
print(is_odd(7.0))
#3.
def is_yes(s):
    if s.lower()== "y" or s.lower() == "yes" or s.lower() == "yeah" or s.lower() == "yup" or s.lower()== "ok" or s.lower()== "sure":
        return True
    else:
        return False
print(is_yes("YEAH!"))
        