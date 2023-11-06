# Time: O(N)
# Space: O(1)
def isRobotBounded(instructions):
    move_facing = {
        'u': (0,1), 
        'd': (0,-1), 
        'l': (-1,0),
        'r': (1,0)
    }

    cycle = {
        'u': 'l',
        'l': 'd', 
        'd': 'r',
        'r': 'u'
    }

    counter_cycle= {
        'u': 'r',
        'r': 'd', 
        'd': 'l',
        'l': 'u'
    }

    cur_pos = [0,0]
    cur_dir = 'u'

    for _ in range(4):
        for instruction in instructions: 
            if instruction == 'G':
                x, y = cur_pos
                i, j = move_facing[cur_dir]
                cur_pos = [x + i, y + j]
            elif instruction == 'L':
                cur_dir = cycle[cur_dir]
            elif instruction == 'R':
                cur_dir = counter_cycle[cur_dir]
    
    return cur_pos == [0,0] 

# instructions = "GGLLGG"
# instructions = "GG"
instructions = "GL"
print(isRobotBounded(instructions))