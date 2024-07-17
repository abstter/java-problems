# ABHIRAM AVASARALA P5

def encrypt_char():
    string = input("What do you want to encrypt? ")
    for i in string:
        if i == ' ':
            print("-", end='')
        elif i == '-':
            print("/", end='')
        elif i == '/':
            print("?", end='')
        elif i == '?':
            print("!", end='')
        elif i == '!':
            print(".", end='')
        elif i == '.':
            print("/", end='')
        elif i == ',':
            print(" ", end='')
        elif i == '0':
            print("1", end='')
        elif i == '1':
            print("2", end='')
        elif i == '2':
            print("3", end='')
        elif i == '3':
            print("4", end='')
        elif i == '4':
            print("5", end='')
        elif i == '5':
            print("6", end='')
        elif i == '6':
            print("7", end='')
        elif i == '7':
            print("8", end='')
        elif i == '8':
            print("9", end='')
        elif i == '9':
            print("0", end='')
        elif i == 'a' or 'b' or 'c' or 'd' or 'e' or 'f' or 'g' or 'h' or 'i' or 'j' or 'k' or 'l' or 'm' or 'n' or 'o' or 'p' or 'q' or 'r' or 's' or 't' or 'u' or 'v' or 'w' or 'x' or 'y' or 'z':
            print(i.upper(), end = '')
        elif i == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I' or 'J' or 'K' or 'L' or 'M' or 'N' or 'O' or 'P' or 'Q' or 'R' or 'S' or 'T' or 'U' or 'V' or 'W' or 'X' or 'Y' or 'Z':
            print(i.lower(), end = '')
        
encrypt_char()            
    

def decrypt():
    string = input("What do you want to decrypt? ")
    for i in string:
        if i == '-':
            print(" ", end='')
        elif i == ' ':
            print("-", end='')
        elif i == '?':
            print("/", end='')
        elif i == '/':
            print("?", end='')
        elif i == '.':
            print("!", end='')
        elif i == '!':
            print(".", end='')
        elif i == ',':
            print("/", end='')
        elif i == '1':
            print("0", end='')
        elif i == '2':
            print("1", end='')
        elif i == '3':
            print("2", end='')
        elif i == '4':
            print("3", end='')
        elif i == '5':
            print("4", end='')
        elif i == '6':
            print("5", end='')
        elif i == '7':
            print("6", end='')
        elif i == '8':
            print("7", end='')
        elif i == '9':
            print("8", end='')
        elif i == '0':
            print("9", end='')
         elif i == 'a' or 'b' or 'c' or 'd' or 'e' or 'f' or 'g' or 'h' or 'i' or 'j' or 'k' or 'l' or 'm' or 'n' or 'o' or 'p' or 'q' or 'r' or 's' or 't' or 'u' or 'v' or 'w' or 'x' or 'y' or 'z':
            print(i.upper(), end = '')
        elif i == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I' or 'J' or 'K' or 'L' or 'M' or 'N' or 'O' or 'P' or 'Q' or 'R' or 'S' or 'T' or 'U' or 'V' or 'W' or 'X' or 'Y' or 'Z':
            print(i.lower(), end = '')

decrypt()
        
        
            
    
    