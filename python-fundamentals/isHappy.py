# isHappy(n)

# this is a solid solution, requires use of hash tables (sets), and that's it!
# runs in whatever the longest cycle of the calcs requried to get to 1 is or to a repeat
# without number theory, I have no idea
# storage is the same complexity: you are storing in the iterations of the cycle\

def isHappy(n):
    def helper (n, container ):
        numstring = str(n)
        sum = 0
        for x in numstring:
            sum += int(x)**2
        if sum == 1: 
            return True
        elif sum not in container: 
            container.add(sum)
            return helper(sum, container)
        else: 
            return False
    return helper(n, set())

print(isHappy(19))
print(isHappy(2))