


def numberOfBeams(bank):
    beam_layers = []
    for row in bank: 
        cur_beams = 0
        for x in row: 
            if x == '1':
                cur_beams +=1
        if cur_beams != 0: 
            beam_layers.append(cur_beams)
    if len(beam_layers) <= 1: 
        return 0
    
    count_beams = 0
    for i in range(1, len(beam_layers)):
        count_beams += beam_layers[i]*beam_layers[i-1]
    return count_beams

bank = ["011001","000000","010100","001000"]

print(numberOfBeams(bank))

