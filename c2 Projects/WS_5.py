# Abhiram Avasarala C5 WS 5

sum=0
def calc_average():
    global sum
    while True:
        for i in range(6):
            sum += float(input("Enter a number: "))
        print("the average of the numbers is " + str(sum/6))
calc_average()