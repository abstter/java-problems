# 10.11.1
def is_reverse(word1, word2):
    if len(word1) != len(word2): # if not even same length
        return False             # can’t be reverse
    i = 0
    j = len(word2)
    while j > 0:
        if word1[i] != word2[j-1]: # if even one char differs
            return False         # can’t be reverse
        i = i + 1         # i traverses word1 forward
        j = j - 1         # j traverses word2 backward
    return True 

print('The words "pots" and "stop" are reversible:', is_reverse('pots', 'stop'))
print('The words "pots" and "spot" are reversible:', is_reverse('pots', 'spot'))

# 10.11.2
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2)
    print('word1 = ', word1, ' word2 = ', word2)
    while j > 0:
        print('i =', i, end = ' ')
        print('word1[', i, '] =', word1[i])
        print('j =', j, end = ' ')
        print('word2[', j, '] =', word2[j])
    if word1[i] != word2[j-1]:
        return False
    i = i + 1
    j = j - 1
    return True

#10.11.3
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2)
    print('word1 = ', word1, ' word2 = ', word2)
    while j >= 0:
        print('i =', i, end = ' ')
        print('word1[', i, '] =', word1[i])
        print('j =', j, end = ' ')
        print('word2[', j, '] =', word2[j])
    if word1[i] != word2[j-1]:
        return False
    i = i + 1
    j = j - 1
    return True

#10.11.4
def is_reverse(word1, word2, case_sense):
    if len(word1) != len(word2):
        return False
    if case_sense == False:
        word1 = word1.lower()
        word2 = word2.lower()
    i = 0
    j = len(word2)
    print('word1 = ', word1, ' word2 = ', word2)
    while j >= 0:
        print('i =', i, end = ' ')
        print('word1[', i, '] =', word1[i])
        print('j =', j, end = ' ')
        print('word2[', j, '] =', word2[j])
    if word1[i] != word2[j-1]:
        return False
    i = i + 1
    j = j - 1
    return True