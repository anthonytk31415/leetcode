def aFunction(a, b):
    print(a, b)
    return a + b


# comments


##########################################################################################
# string methods 
##########################################################################################

mystring = 'hello'
len(mystring)
# 5

# triple quotes allow for returns in quotations
print('''My instructions are very long so to make them
more readable in the code I am putting them on
more than one line. I can even include "quotes"
of any kind because they won't get confused with
the end of the string!''')

## indexing

## 
mystring[1:] # e

mystring[1:] # ello
## does not include the last index
mystring[1:4] # ell


mystring.index('e') ## like indexOf() in js - returns first index of the searched string
mystring.rindex('e') ## returns first index of the string coming from the right


## assigning variables to strings to print
a1 = 'Wednesday'
a2 = 'series'
print('i am watching the {0} {1}'.format(a1, a2))

## turns upper; lower; boolean checks
a1.upper()
a1.lower()
a1.isupper()
a1.islower()

sentence = 'I mean, I could give you a million excuses'
sentence.split()  ## returns array with substrings separated by spaces

s = "i-am-a-dog"	
s.split("-") ## returns array of words separated by '-'

shopping_list = ['bread','milk','eggs']
', '.join(shopping_list) ## joins array of strings with the char specified 



### is palindrome 


## while loop
x = 3
while x > 0: 
    print(x)
    x -=1


def is_palindrome(word):
    counter = len(word)/2
    index = 0
    while index <= counter:
        if word[index] != word[-1 - index]: 
            return False
        index +=1
    return True




## rounding
round(len('brady')/2) # round down

## recursive reverse string
def reverse_string(word):
    if len(word) == 0:
        return ''
    else:
        return word[-1] + reverse_string(word[0:-1])



def last_index(word, char_search):
    reverse_word = reverse_string(word)
    return ( len(word) - ( reverse_word.index(char_search) + 1))



def blah():
    return 


## fib

def recursive_fib(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else: 
        return recursive_fib(x - 1) + recursive_fib(x - 2)



## is_prime(n)

def is_prime(x, n=2): 
    if x == 1:
        return False
    elif x == n: 
        return True
    elif x % n == 0: 
        return False
    else: 
        return is_prime(x, n+1)


def reverse_string(word):
    if len(word) == 0:
        return ''
    else:
        return word[-1] + reverse_string(word[0:-1])

def last_index(word, char_search):
    reverse_word = reverse_string(word)
    return ( len(word) - ( reverse_word.index(char_search) + 1))



def first_before_second(phrase, a, b): 
    def reverse_string(word):
        if len(word) == 0:
            return ''
        else:
            return word[-1] + reverse_string(word[0:-1])

    def last_index(word, char_search):
        reverse_word = reverse_string(word)
        return ( len(word) - ( reverse_word.index(char_search) + 1))

    return last_index(phrase,a) < phrase.index(b)




# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, 
# formed from three of these lengths. If it is impossible to form any triangle of a 
# non-zero area, return 0.

# largest perimeter



# regular expressions
import re
bool(re.match('^[a-zA-Z0-9]+$', '789def')) ## checks if alphanumeric 