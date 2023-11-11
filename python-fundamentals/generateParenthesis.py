# start with 

def generateParenthesis(n):

    res = set()

    def dfs(opens, closes, current):
        if opens == 0: 
            strCloses = ")" * closes
            final = current + strCloses
            res.add(final)
            return 

        # open and close > 0:
        openPath = []
        if opens > 0: 
            dfs(opens-1, closes + 1, current + "(")
        closePath = []
        if closes > 0: 
            dfs(opens, closes - 1, current + ")")

    dfs(n, 0, "")
    return res



print(")"*3)
a = ["a", "b"]
c = ["c"]
print(a + c)
print(["d" + x for x in a])

print(generateParenthesis(3))