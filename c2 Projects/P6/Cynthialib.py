"""
Project #1: Crazy Libs
Python Level 2
"""

author = 'Cynthia Wang'

def crazy_lib():
    print ("Welcome to Cynthia's Crazy Lib!")
    animal = input ('Enter an animal: ')
    name = input ('Enter a name (capitalized): ')
    place = input ('Enter the name of a made-up land or country (capitalized): ')
    disease = input ('Enter the name of a disease (made-up, capitalized): ')
    verb = input ('Enter a present-tense verb: ')
    adverb = input ('Enter an adverb ending with -ly: ')
    dessert = input ('Enter a dessert: ')
    color = input ('Enter a color: ')
    spice = input ('Enter a spice: ')
    landform = input ('Enter a landform: ')
    name2 = input ('Enter a name (capitalized): ')
    number2 = input ('Enter a number: ')
    time = input ('Enter a plural unit of time (eg. hours, days, years): ')
    animal2 = input ('Enter an animal: ')
    name3 = input ('Enter a name (capitalized): ')
    liquid = input ('Enter a liquid: ')
    adjective = input ('Enter an adjective: ')
    made_up_word = input ('Enter a made-up word (capitalized): ')
    verb2 = input ('Enter a past-tense verb: ')
    adjective2 = input ('Enter an adjective: ')
    color2 = input ('Enter a color: ')
    noun = input ('Enter a plural noun: ')
    body_part = input ('Enter a body part: ')
    print ('\n')
    print ('Once upon a time, there was a', animal, 'named', name, '\nwho lived in a land called ' + str(place) + '.')
    print (name, 'was born with a disease known as ' + str(disease) + ',\nwhich rendered him unable to ' + str(verb) + ' ' + str(adverb) + '.')
    print (disease, 'also gave him a strange addiction to ' + str(dessert) + ',\nbut only when it was', color, 'and sprinkled with ' + str(spice) + '.')
    print (name, 'journeyed to a', landform, 'known as Mt.', name2, 'to search for a cure.')
    print ('After', number2, time, 'of searching, he met a', animal2, 'by the name of ' + str(name3) + '.')
    print (name3, 'presented him with a bottle of', adjective, liquid, 'he called', made_up_word, '\nand claimed could heal ' + str(disease) + '.')
    print (name, verb2, 'the liquid but found that he had developed a case of\n', adjective2, color2, noun, 'all over his ' + str(body_part) + '.')

