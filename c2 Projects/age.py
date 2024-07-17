def age_menu():
    print('\n << Age Calculator Menu: >>')
    print('1. Calculate your age in months')
    print('2. Calculate your age in days')
    print('3. Calculate your age in hours')
    print('4. Quit')
    ans = int(input('\nEnter your choice from the menu: '))
    while ans <= 4:
        if ans == 1:
            age = int(input('Enter your age in years: '))
            print('You are about', age*12, 'months old.')
        elif ans == 2:
            age = int(input('Enter your age in years: '))
            print('You are about', age*365, 'days old.')
        elif ans == 3:
            age = int(input('Enter your age in years: '))
            print('You are about', age*365*24, 'hours old.')
        elif ans == 4:
            print('Thanks for using the Age Calculator! Goodbye!')
        else:
            print('Invalid input! Please try again.')
    
age_menu()