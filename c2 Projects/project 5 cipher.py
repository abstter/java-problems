# Abhiram Avasarala C5 Project 5

original_alphabet =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,.!?/-'
cipher_key = ["86Y?2OP9,AG1ZV5SN7M'JEBTIHCX.KW0FQ- DU!34LR","J5E!MWNOPQF24?7,ZYUX9G6K381 HLRI0T'DCBV-AS.","5QZKBDG' AP-802UW.3!EH7VI,JC9RLX?TN61FOY4MS","L?XUEDTRBQNJHS2!1.F6 MC3IZ4Y5K'AVP0O-978W,G","PBCRNH!JW3M17Q0US2KTOL'EA4.XV, 9D6-IF8GY5Z?"]

def encrypt(): #This function takes the original alphabet then the cipher and encrypts the sentence to a cipher
    user_input = input("Enter a value for ciphering: ").upper()# This line asks the user for a value to be encrypted
    i = 0
    for char in user_input:
        gi = original_alphabet.index(char) 
        j = i % 5
        print(cipher_key[j][gi],end = '')
        i = i + 1
encrypt()

def decipher(): #This function takes the cipher then the original alphabet and decrypts the cipher to the sentence
    user_input = input("Enter a value for deciphering: ").upper() #This line asks the user for a value for deciphering
    i = 0
    for char in user_input:
        j = i % 5
        gi = cipher_key[j].index(char) 
        print(original_alphabet[gi], end = '')
        i = i + 1
decipher()

'''
Output Files

Enter a value for ciphering: HONEY WHERE ARE THE COOKIES
970EAD6'E22C5.NDX'EFY72NW2UEnter a value for deciphering: 970EAD6'E22C5.NDX'EFY72NW2U
HONEY WHERE ARE THE COOKIES

'''
    
    
    