# https://leetcode.com/problems/wildcard-matching/

* = any sequence (of any size)
? = any single char
What are the types of searches: 


*** this is redundant
*a* {any} a {any}
*a?a*
a*? a {any} {any char}
ab*cd*? --> ab {any} cd {any} {any char}
*cd*bc?
# if it's just a string, then you just go by i, j like a two pointer question
# when you hit the * in the evaluation, you need to treat it like: 
# of the remainder of the string, does ____ occur? 
# after a *, take the first occurrence of the pattern, if it matches, then move on; 

cdxxxxxcdaxxxbca


def isMatch(s, p):