'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

""" 
declare sub-string we will look for, "th"
input the word string into the function
if input is not a string or has len of 1 or -, exit function, return -
function: 
    search the left-most character i of the word the letter "t" and i+1 for "h"
    if true add 1 to count 
    set word to wrod minus 1 index
call function again until only 1 character in word left.

"""



def count_th(word):
    substring = "th"
    if len(word) < 2:
        return 0 
    elif word[:2] == substring: 
        return 1 + count_th(word[1:])
    else: 
        return count_th(word[1:])
    return result
    
    word = "abcthxyz"
    x = count_th(word)
    print(x)
    word = "abcthefthghith"
    print(count_th(word))
    word = ""
    print(count_th(word))


    pass

# Ran 5 tests in 0.000s  OK
