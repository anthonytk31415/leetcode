from random import randint

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)
    

d_six = Die(6)
d_eight = Die(8)

# print(d_six.roll(),
#     d_six.roll(),
#     d_six.roll(),
#     d_eight.roll(),
#     d_eight.roll(),
#     d_eight.roll(),)


class WeaponDmg:
    def __init__(self, modifier, roll_arr):     # roll_arr[i] = [num_rolls, sides_of_die]
        self.modifier = modifier
        self.roll_arr = roll_arr
        self.dice = {}
        self.populate_dice()

    def populate_dice(self):
        for (num_rolls, sides) in self.roll_arr: 
            self.dice[sides] = Die(sides)

    def calc_dmg(self, crit):
        total_dmg = 0
        crit_mod = 1
        if crit==1: 
            crit_mod = 2
        for (num_rolls, sides) in self.roll_arr: 
            for _ in range(num_rolls*crit_mod): 
                total_dmg += self.dice[sides].roll()
        return total_dmg + self.modifier
    


axe = WeaponDmg(4, [[2,6]])
print(axe.calc_dmg(1))

class AttackRoll:
    def __init__(self, modifier, ar):
        self.modifier = modifier
        self.ar = ar
        self.die = Die(20)

    def atk_roll(self):         # returns [hit_success (T/F), 0/1/2] 0 = normal, 1 = crit; 2 = automiss
        die_roll = self.die.roll()
        hit_success = die_roll + self.modifier >= self.ar
        nat = 0
        if die_roll == 20: 
            nat = 1
        elif die_roll == 1:
            nat = 2
        return [hit_success, nat]
    
golem = AttackRoll(4, 18)
print(golem.atk_roll(), golem.atk_roll(), golem.atk_roll(), )


class FightCommand:
    def __init__(self, weapon_mod, weapon_roll_arr, armor_mod, ar):
        self.atk_success = AttackRoll(armor_mod, ar)
        self.weapon = WeaponDmg(weapon_mod, weapon_roll_arr)

    def calc_dmg(self):
        atk = self.atk_success.atk_roll()
        if atk[0]:
            if atk[1] != 2:
                dmg = max(1, self.weapon.calc_dmg(atk[0]))
                if atk[1] == 1: 
                    print('crit! dmg: ', dmg)
                else: 
                    print('dmg: ', dmg)
                return dmg
            else:   # miss due to nat1
                print('nat1 miss!!')
                return 0
        else:   # miss due to armor
            print('ar miss!')
            return 0
        
axe_vs_ogre = FightCommand(4, [[2,6]], 3, 4)

for _ in range(10):
    print(axe_vs_ogre.calc_dmg())