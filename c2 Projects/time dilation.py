import time,re
import math
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

time_dilation_calc()