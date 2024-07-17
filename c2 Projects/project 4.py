def encrypt_char(char):
    normal = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ,.!?/-'
    new = '-/?!.,ABCdEfghijklmnopqrstuvwxyzABCd1234567efghijklmnopqrstuvwxyz890 '
    index = normal.index(char)
    new_char = new[index]
    return new_char

def decrypt_char(char):
    normal = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ,.!?/-'
    new = '-/?!.,ABCdEfghijklmnopqrstuvwxyzABCd1234567efghijklmnopqrstuvwxyz890 '
    index = normal.index(char)
    new_char = new[index]
    return new_char