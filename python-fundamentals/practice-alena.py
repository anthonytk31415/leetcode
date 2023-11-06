# a = 0

# def increment1(val):
#     val +=1

#     return val

# increment1(a)

# print(a)   #prints 0


# a = {'name':'alena'}


# def increment2(str):
#     str['name'] += ' sim'


# increment2(a)
# print(a)


class Gamestate: 
    def __init__(self): 
        self.score = 0

    def increaseScore(self):
        self.score +=1


game = Gamestate()
print(game.score)
game.increaseScore()

print(game.score)