"""
Worksheet # 9: Basic List Operations
Examples and Solutions
Python Level 2
"""

import array

print('\n *** Problem 1 *** ')

# Uncomment each code block below to test it, and then comment it
# out again when done so it doesn't affect the other code results.

socmed = ['Facebook', 'TikTok', 'Twitter', 'Instagram']

print('\n ** Problem 1a: ')
#socmed[0] = 'Metaverse?'
#socmed[4] = 'YouTube'

print('\n ** Problem 1b: ')
#socmed.extend(['WhatsApp', 'Telegram'])
#print(len(socmed))

print('\n ** Problem 1c: ')
#socmed.append(['WhatsApp', 'Telegram'])
#print(len(socmed))

print('\n ** Problem 1d: ')
#platform = socmed.pop(2)
#platform[6] = 'd'

   
print('\n\n *** Problem 2 *** \n')

sched = ['Mon', 'Wed', 'Fri']

#sched = sched + 'Sat'
#sched.extend('Sat')
sched.append('Sat')   

#print('sched:', sched)


print('\n\n *** Problem 3 *** \n')
sched.insert(1, 'Tue')

print('sched:', sched) # To test the insert() statement

print('\n\n *** Problem 5 *** \n')

numbers = [9, 5, 11, 8, 10, 100, 6, 15]

def max10_list(nums):
    for i in range(len(nums)):
        if nums[i] > 10:
            nums[i] = 10
    return nums
    
new_numbers = max10_list(numbers)

# code to test max10_list()
print ('Original list: ', numbers)
print ('After calling max10_list(): ', new_numbers)


print('\n\n *** Problem 6 *** \n')

# extend_list(list1, list2) should mimic how the list.extend()
# method works, just adding all the items from list2 to list1
# without making a third, new list.

        
# Code to test extend_list() below; uncomment to test:
def extend_list(list1, list2):
    list1.append(list2)
    return list1
# Ron's schedule:
ron_sched = ['Mon', 'Tue', 'Thu']

# Ron and Ira work together as partners, so they should have 
# identical schedules for the foreseeable future. We use separate
# variables just in case their schedules are ever decoupled.
# We will have ira_sched refer to the list in ron_sched so that
# it will mirror whatever is in that list.
ira_sched = ron_sched  

# First, let\'s check both schedules, verifying that they start off
# the same since ira_sched points to the same list as ron_sched:
print("Ron's and Ira's schedules must always remain identical:\n")
print("Ron's schedule:", ron_sched)
print("Ira's schedule:", ira_sched)

# Now, we update Ron\'s schedule by adding some days to it
# using concatenate (+)
ron_sched = ron_sched + ['Fri', 'Sat', 'Sun']

# Now, let's print Ron's and Ira's schedule, which are supposed to
# stay the same (but we'll find that they're not the same after 
# using + to extend ron_sched above):
print("\nAfter concatenating Ron\'s schedule (using +) with",
      "['Fri', 'Sat', 'Sun']:\n")
print("Ron's schedule:", ron_sched)
print("Ira's schedule:", ira_sched)

# As you will see from the test output, Ira's schedule is no longer
# the same as Ron's because concatenate (+) made an entirely new 
# list. So, ron_sched was assigned to an entirely different list in
# the + statement above, decoupling it from ira_sched.

# Next, let's reset ron_sched and ira_sched to test extend_list()
# on them and see how it works differently from +
print("\nResetting Ron's and Ira's schedules...")
ron_sched = ['Mon', 'Tue', 'Thu']
ira_sched = ron_sched

# We use extend_list() instead of concatenate this time:
extend_list(ron_sched, ['Fri', 'Sat', 'Sun'])

# Now, let's print the schedules after using extend_list().
print("\nAfter using extend_list() to add ['Fri', 'Sat', 'Sun'] to","Ron's schedule:\n")
print('Ron\'s schedule:', ron_sched)
print('Ira\'s schedule:', ira_sched)

# That time, Ira's schedule should have updated as well, because
# ira_sched still points to the same list as ron_sched. extend_list()
# just extended that list rather than making a new one altogether.


print('\n\n *** Problem 7 *** \n')

nums1 = [3, 5, 1, 8]
nums2 = [2, 4, 3, 19]


    
#prod_nums = mult(nums1, nums2)
#print('nums1:', nums1)
#print('nums2:', nums2)
#print('prod_nums:', prod_nums)


print('\n\n *** Problem 8 *** \n')

car = ['Toyota', 'Prius', ['City', 58], ['Highway', 53]]
print(car[1] + ": " + car[2][0] + ": " + str((car[3][1]+5)) + 'mpg.')


print('\n\n *** Problem 9 *** \n')

calendar = [['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
            [' ', ' ', 1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10, 11, 12],
            [13, 14, 15, 16, 17, 18, 19],
            [20, 21, 22, 23, 24, 25, 26],
            [27, 28, 29, 30, 31]]

for i in calendar:
    print('\n')
    for j in i:
        print(str(j).ljust(3, ' '), end=' ')

'''
 *** Problem 5 *** 

Original list:  [9, 5, 10, 8, 10, 10, 6, 10]
After calling max10_list():  [9, 5, 10, 8, 10, 10, 6, 10]


 *** Problem 6 *** 

Ron's and Ira's schedules must always remain identical:

Ron's schedule: ['Mon', 'Tue', 'Thu']
Ira's schedule: ['Mon', 'Tue', 'Thu']

After concatenating Ron's schedule (using +) with ['Fri', 'Sat', 'Sun']:

Ron's schedule: ['Mon', 'Tue', 'Thu', 'Fri', 'Sat', 'Sun']
Ira's schedule: ['Mon', 'Tue', 'Thu']

Resetting Ron's and Ira's schedules...

After using extend_list() to add ['Fri', 'Sat', 'Sun'] to Ron's schedule:

Ron's schedule: ['Mon', 'Tue', 'Thu', ['Fri', 'Sat', 'Sun']]
Ira's schedule: ['Mon', 'Tue', 'Thu', ['Fri', 'Sat', 'Sun']]


 *** Problem 7 *** 



 *** Problem 8 *** 

Prius: City: 58mpg.


 *** Problem 9 *** 



Sun Mon Tue Wed Thu Fri Sat 

        1   2   3   4   5   

6   7   8   9   10  11  12  

13  14  15  16  17  18  19  

20  21  22  23  24  25  26  

27  28  29  30  31 

'''