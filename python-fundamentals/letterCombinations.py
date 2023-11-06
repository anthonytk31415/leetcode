# letterCombinations


# def letterCombinations(digits):
#     alpha = 'abcdefghijklmnopqrstuvwxyz'
#     alphaDict = {}
#     for i in range(2,10):
#         key = str(i)
#         if i ==7 or i ==9:
#             alphaDict[key] = alpha[0:4]
#             alpha = alpha[4:]
#         else:
#             alphaDict[key] = alpha[0:3]
#             alpha = alpha[3:]
#     container = []
#     for n in digits:
#         letters = alphaDict[n]
#         if len(container) == 0:
#             container = [letter for letter in letters]
#         else: 
#             container = [x+y for x in container for y in letters]
#     return container





def letterCombinations(digits):
    alphaDict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    container = []
    for n in digits:
        letters = alphaDict[n]
        if len(container) == 0:
            container = [letter for letter in letters]
        else: 
            container = [x+y for x in container for y in letters]
    return container


print(letterCombinations('92'))