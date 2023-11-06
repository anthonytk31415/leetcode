#findwords
    # then build a next step of letters iteratively
## give series of letters that are equal to the first letter in a word to iterate over



# given the board, position (e.g. (1,2)),and letter (e.g. 'a'), and checked, 
# return an array with tuples of two items: [item1, item 2, ...] 
# item[0] = an array of valid positions where those positions = letter
# item[1] = checked filled in 
# i.e. res = candidate pairs 

# print('hello new ')

# def candidates(board, position, letter, checked):
#     x0 = 0
#     x1 = len(board) - 1
#     y0 = 0
#     y1 = len(board[0]) - 1
#     (x,y) = position
#     potential = ([(x + i, y) for i in [-1,1] if x + i >= x0 and x + i <= x1] + 
#                  [(x, y + j) for j in [-1,1] if y + j >= y0 and y + j <= y1] )
#     # print(f'potential : {potential}')
#     res = []
#     for z in potential:
#         if board[z[0]][z[1]] == letter and z not in checked:
#             checked_copy = set(list(checked))
#             # print(checked_copy)
#             checked_copy.add(z)
#             res.append((z, checked_copy))
#     return res


# ## given a letter on a board, 
# ## letter = (i,j)
# ## assume letter coordinate equals first letter of word
# def findWordWithLetter(board, word):
#     # is the first word there? 
#     # for each element on the board, return starting positions

#     candidate_pairs = []     #array of coordinates that are first letters of the searched word; for x in candidates -> x[0] = coordinates in board; x[1] = checked = {(i,j), }
#     if len(word) == 0:
#         return True
#     letter = word[0]
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] == letter:
#                 candidate_pairs.append(( (i,j) , {(i,j), } ))

#     print(f'letter = {letter}, 1st cp: {candidate_pairs}')
#     def helper(board, candidate_pairs, word):
#         if len(word) == 0:
#             print(f'True: word = {word}, cp = {candidate_pairs}')
#             return True
#         elif len(word) > 0 and len(candidate_pairs) == 0:
#             return False
#         else: 
#             letter = word[0]
#             new_word = word[1:]
#             new_candidate_pairs = []
#             print(f'og cp: {candidate_pairs}')
#             for x in candidate_pairs: #for each pair, find the next letter
#                 position = x[0]
#                 checked = x[1]
#                 new_candidate_pairs.append(candidates(board, position, letter, checked))
#             print(f'letter = {letter}; new cp: {new_candidate_pairs}')
#             return any([helper(board, x, new_word) for x in new_candidate_pairs if len(x)>0])

#     return helper(board, candidate_pairs, word[1:])


board = [["o","t","z","w"],["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
position = (1,0)
letter = 'a'
checked = set()
checked.add(position)

# print(candidates(board, position, letter, checked))






# iterate over an array of words
def findWords(board, words):
    def candidates(board, position, letter, checked):
        x0 = 0
        x1 = len(board) - 1
        y0 = 0
        y1 = len(board[0]) - 1
        (x,y) = position
        potential = ([(x + i, y) for i in [-1,1] if x + i >= x0 and x + i <= x1] + 
                    [(x, y + j) for j in [-1,1] if y + j >= y0 and y + j <= y1] )
        # print(f'potential : {potential}')
        res = []
        for z in potential:
            if board[z[0]][z[1]] == letter and z not in checked:
                checked_copy = set(list(checked))
                # print(checked_copy)
                checked_copy.add(z)
                res.append((z, checked_copy))
        return res

    def findWordWithLetter(board, word):
        # is the first word there? 
        # for each element on the board, return starting positions

        candidate_pairs = []     #array of coordinates that are first letters of the searched word; for x in candidates -> x[0] = coordinates in board; x[1] = checked = {(i,j), }
        if len(word) == 0:
            return True
        letter = word[0]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == letter:
                    candidate_pairs.append(( (i,j) , {(i,j), } ))
        if len(candidate_pairs) == 0:
            return False
        # print(f'letter = {letter}, 1st cp: {candidate_pairs}')

        def helper(board, candidate_pairs, word):
            if len(word) > 0 and len(candidate_pairs) == 0:
                return False
            elif len(word) == 0:
                # print(f'True: word = {word}, cp = {candidate_pairs}')
                return True

            else: 
                letter = word[0]
                new_word = word[1:]
                new_candidate_pairs = []
                # print(f'og cp: {candidate_pairs}')
                for x in candidate_pairs: #for each pair, find the next letter
                    position = x[0]
                    checked = x[1]
                    new_candidate_pairs.append(candidates(board, position, letter, checked))
                # print(f'letter = {letter}; new cp: {new_candidate_pairs}')
                return any([helper(board, x, new_word) for x in new_candidate_pairs if len(x)>0])

        return helper(board, candidate_pairs, word[1:])


    res = []
    for word in words: 
        if findWordWithLetter(board, word):
            res.append(word)
    return res


board_a = [   ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"],
            ["a","a","a","a","a","a","a","a","a","a","a","a"]]

words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

# print(findWords([["a"]], ["b"]))

print(findWords(board_a, words))