# 2:15

def parse_morse(signal):
    signal = [str(x) for x in signal]
## separate 1 and 0
    res = []
    cur = signal[0]
    last = signal[0]
    for i in range(1,len(signal)):
        if signal[i] == last: 
            cur = cur + signal[i]
        else: 
            res.append(cur)
            cur = signal[i]
        last = signal[i]
    res.append(cur)

    res_final = []
    for x in res: 
        if x == '1' or x == '11':
            res_final.append('.')
        elif x == '111' or x == '1111' or x == '11111':
            res_final.append('-')
        elif x == '0' or x == '00':                         #a new "blip"
            res_final.append('')
        elif x == '000' or x == '0000' or x == '00000':
            res_final.append(' ')                           # a new letter is next
        elif x == '000000':                                 # spaces between words
            res_final.append('*')
    print(res)
    return res_final
# signal = [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1]

# print(parse_morse(signal))

# . = 1 or 2 '1'





alpha = {
".-": "a",
"-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z",
}

# print(alpha['.-'])


def parse_strings(signal):
    signal = parse_morse(signal)
    print(signal)
    letters = []
    cur = ''
    #join together "." and "-" to form a word by looking for spaces and empty chars
    for x in signal: 
        if x == '':                     # if '' then add to curr (its part of the same letter)
            continue
        elif x == ' ':                  # ' ' signifies new letter coming up next
            letters.append(cur)
            cur = ''
        elif x == '*':
            letters.append(cur)
            letters.append(' ')
            cur = ''
        else:
            cur = cur + x
    if cur != '':
        letters.append(cur)
    
    res = ''
    for x in letters:
        if x == ' ':
            res = res + ' '
        else: 
            res = res + alpha[x]
    print(res)
    return res


signal= [0,1,1,0,1,1,1,0,0,1,1,1,1,0,1,1,1,1,1,0,0,0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0]
parse_strings(signal)