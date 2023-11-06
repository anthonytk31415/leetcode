# sq interview question 

cards = [
{ 'suit': "heart", 'rank': "8" },
{ 'suit': "diamond", 'rank': "2" },
{ 'suit': "diamond", 'rank': "ace" },
{ 'suit': "heart", 'rank': "king" },
{ 'suit': "spade", 'rank': "4" },
{ 'suit': "club", 'rank': "king" },
{ 'suit': "spade", 'rank': "king" },
{ 'suit': "heart", 'rank': "4" }
]

from collections import defaultdict


s_suit = {'heart': 'h', 'spade': 's', 'diamond': 'd', 'club': 'c'}

def frequency(cards):
    res = defaultdict(int)
    for x in cards: 
        print(x['rank'])
        res[x['rank']] +=1
    return res

freq_cards=  frequency(cards)
print(freq_cards)

# returns hash table of rank:value key:value pairs
def card_values():
    res = {'jack': 10,
            'queen':10,
            'king':10,
            'ace':1,}
    for i in range(2, 11):
        res[str(i)] = i
    return res

card_val = card_values()

print(card_val)

# given a hand of cards, returns hand value
def hand_val(cards):
    card_val = card_values()
    return sum([card_val[card['rank']] for card in cards])

print(hand_val(cards))

# returns who wins; hand_p > hand_d --> true else false (note dealer wins ties)
def player_wins(p_cards, d_cards):
    return hand_val(p_cards) > hand_val(d_cards)

## takes a card, returns k-shifted card
## a > 2 for k = 1
## 8 > J for k = 3
def shift_card(card, k):
    card_order = ['ace', '2','3','4','5','6','7','8','9','10','jack','queen','king']
    k = k % 13                      
                                    # only traverse 13 cards
    card_val = card_values()        # note this returns the index in card order; need to minus one to match array

    cur_idx = card_order.index(card['rank'])
    idx = (cur_idx + k )% 13
    new_rank = card_order[idx]
    card['rank'] = new_rank
    return card

def shift_hand(cards):
    return [shift_card(card, -13) for card in cards]

# print(shift_hand(cards))

## if both ranks are in hand
## values is an array of 2 values: (a,b) values to swap
def swap(cards, values):
    a,b = values
    swapper = {a:b, b:a}
    card_values = [card['rank'] for card in cards]
    if a in card_values and b in card_values: 
        for card in cards:
            if card['rank'] in swapper:  
                card['rank'] = swapper[card['rank']]
    return cards


# print(swap(cards, ['2','king']))

def swap_full(cards, values):
    card1, card2 = values
    suit1, suit2 = card1['suit'], card2['suit']
    rank1, rank2 = card1['rank'], card2['rank']
    suit_swapper = {suit1:suit2, suit2:suit1}
    rank_swapper = {rank1:rank2, rank2:rank1}


    if card1 in cards and card2 in cards: 

        for card in cards:
            if card == card1 or card == card2: 
                card['suit'] = suit_swapper[card['suit']]
                card['rank'] = rank_swapper[card['rank']]
    return cards

# print(swap_full(cards, [{ 'suit': "spade", 'rank': "king" }, { 'suit': "heart", 'rank': "4" }]))




# brute force with combinations 

from itertools import combinations
# from the cards, find all possible combinations of hands that'll beat the dealer:  
def winnings_hands(cards, dealer_val):
    s_suit = {'heart': 'h', 'spade': 's', 'diamond': 'd', 'club': 'c'}
    card_val = card_values()
    cards_new = [(card_val[card['rank']], s_suit[card['suit']]) for card in cards]       ## holds the tuple if (card val, card) so you can pay attn to the card val itself
    cards_new.sort(key = lambda x: -x[0])

    combos = []
    for i in range(1, len(cards_new)+1):
        combos = combos + list(combinations(cards_new, i))
    print(combos)
    winning_hands = []
    for x in combos: 
        if sum([y[0] for y in x]) > dealer_val: 
            winning_hands.append(x)
    # winning_hands = [x for x in combos if sum([y[0] for y in x]) > dealer_val ]
    # winning_hands = [[str(x[0]) + str(x[1]) for x in y] for y in winning_hands]
    return winning_hands
    # print(cards_new)
w1 =  winnings_hands(cards, 3)
print('1', w1)


def winnings_hands2(cards, dealer_val):
    s_suit = {'heart': 'h', 'spade': 's', 'diamond': 'd', 'club': 'c'}
    card_val = card_values()
    cards_new = [(card_val[card['rank']], s_suit[card['suit']]) for card in cards]       ## holds the tuple if (card val, card) so you can pay attn to the card val itself
    cards_new.sort(key = lambda x: -x[0])                            
    combos = []


    def helper(cards, combos, cur, dealer_val):
        if sum([x[0] for x in cards]) < dealer_val: 
            return 
        if dealer_val < 0:
            combos.append(cur)
            if not cards: 
                return 
        for i in range(len(cards)):
            helper(cards[i+1:], combos, cur + [cards[i]], dealer_val - cards[i][0])


    helper(cards_new, combos, [], dealer_val)
    combos = [[str(x[0])+ str(x[1]) for x in y] for y in combos]
    return combos
w2 = winnings_hands2(cards, 3)
print('2', w2)

print(len(w1))
print(len(w2))
# given an array of objects return all possible combinations

# abc  --> 
# a, b, c, ab, ac, 
# bc, abc

def combination(arr):
    res = ['']
    for x in arr: 
        new_res = [y + x for y in res]
        res = res + new_res
    return res

# print(combination('abc'))

