from random import randint, shuffle


def themselvesAssignment(arrNames, assignment):
    for i in range(len(arrNames)):
        if arrNames[i] == assignment[i]:
            return False
    return True

def secretSantaAssignment(arrNames):
    assignment = [x for x in arrNames]
    shuffle(assignment)
    while themselvesAssignment(arrNames, assignment)== False:
        shuffle(assignment)
    return assignment

arrNames = ['tina', 'angela', 'billy', 'anthony', 'janice']
print(secretSantaAssignment(arrNames))