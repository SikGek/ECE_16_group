import enchant as e
import numpy as np
dictionary = e.Dict('en_US')

def english_to_pig_latin(str):
    vow = ['a', 'A', 'e', 'E', 'i','I', 'o', 'O', 'u', 'U', 'y', 'Y']
    vow_wo_u = ['a', 'A', 'e', 'E', 'i','I', 'o', 'O', 'y', 'Y']
    vow_wo_y = ['a', 'A', 'e', 'E', 'i','I', 'o', 'O', 'u', 'U']
    if '-' in str:
        str = str.split('-')
        if len(str) == 2:
            str1 = english_to_pig_latin(str[0])
            str2 = english_to_pig_latin(str[1])
            str = str1 + '-' + str2
        elif len(str) == 3:
            str1 = english_to_pig_latin(str[0])
            str2 = english_to_pig_latin(str[1])
            str3 = english_to_pig_latin(str[2])
            str = str1 + '-' + str2 + '-' + str3
    else:       
        if str[0] not in vow and (str[:2] != 'qu' and str[:2] != 'Qu'):
            while str[0] not in vow:
                str = str + str[0]
                str = str[1:]
            str = str + 'ay'
        elif str[0] == 'y' or str[0] == 'Y':
            while str[0] not in vow_wo_y:
                str = str + str[0]
                str = str[1:]
            str = str + 'ey'
        elif str[0] in vow and str[0] != 'y' and str[0] != 'Y':
            str = str + 'yay'
        elif (str[0] == 'q' or str[0] == 'Q') and (str[1] == 'u' or str[1] == 'U'):
            while str[0] not in vow_wo_u:
                str = str + str[0]
                str = str[1:]
            str = str + 'ay'
    if '!' in str:
        str = str.replace("!", '')
        str = str + '!'
    elif '?' in str:
        str = str.replace('?', '')
        str = str + '?'
    return str


def pig_latin_to_english(stri):
    if '-' in stri:
        stri = stri.split('-')
        if len(stri) == 2:
            stri1 = pig_latin_to_english(stri[0])
            stri2 = pig_latin_to_english(stri[1])
            stri = stri1 + '-' + stri2
        elif len(stri) == 3:
            stri1 = pig_latin_to_english(stri[0])
            stri2 = pig_latin_to_english(stri[1])
            stri3 = pig_latin_to_english(stri[2])
            stri = stri1 + '-' + stri2 + '-' + stri3
    if stri[-3:] == 'yay':
        stri = stri[0:-3]
    elif stri[-2:] == 'ey':
        stri = stri[0:-2]
        stri = stri[-1] + stri
        stri = stri[0:-1]
    elif stri[-2:] == 'ay':
        stri = stri[0:-2]
        stri = stri[-1] + stri
        stri = stri[0:-1]
    if '!' in stri:
        stri = stri.replace("!", '')
        if stri[-3:] == 'yay':
            stri = stri[0:-3]
        elif stri[-2:] == 'ey':
            stri = stri[0:-2]
            stri = stri[-1] + stri
            stri = stri[0:-1]
        elif stri[-2:] == 'ay':
            stri = stri[0:-2]
            stri = stri[-1] + stri
            stri = stri[0:-1]
        while dictionary.check(stri) == False:
            stri = stri[-1] + stri
            stri = stri[0:-1]
        stri = stri + '!'
    elif '?' in stri:
        stri = stri.replace('?', '')
        if stri[-3:] == 'yay':
            stri = stri[0:-3]
        elif stri[-2:] == 'ey':
            stri = stri[0:-2]
            stri = stri[-1] + stri
            stri = stri[0:-1]
        elif stri[-2:] == 'ay':
            stri = stri[0:-2]
            stri = stri[-1] + stri
            stri = stri[0:-1]
        while dictionary.check(stri) == False:
            stri = stri[-1] + stri
            stri = stri[0:-1]
        stri = stri + '?'
    else:
        while dictionary.check(stri) == False:
            stri = stri[-1] + stri
            stri = stri[0:-1]
    return stri

test_list = ['Quotient','Mustn\'t','Yellow', 'Honest', 'Thursday', 'Christmas', 
             'Alliteration', 'Information', 'Education', 'Fish', 'Numbers!', 
             'Toyota?', 'Mother-in-law', 'Laps', 'Slap', 'August', 'empty-handed',
             'Ice-cream', 'Years', 'Yankee', 'Yawn', 'Young', 'Yard', 'Quiet', 'Quack']

for i, word in enumerate(test_list):
    out1 = english_to_pig_latin(word)  
    out2 = pig_latin_to_english(out1)
    print(i+1, 'inputted word:', word)
    print(i+1, 'english -> p-latin:', out1)
    print(i+1, 'p-latin -> english:', out2)