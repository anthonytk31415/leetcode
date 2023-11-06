def judgeCircle(moves):
    y = {'U': 1, 'D':-1}
    x = {'L':1, 'R':-1}
    pos = [0, 0]
    for m in moves:
        if m in x: pos[0] +=x[m]
        else: 
            pos[1] +=y[m]
    return pos == [0,0]

# Time: O(n)
# Space: O(1)