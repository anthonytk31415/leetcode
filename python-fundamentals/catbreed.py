# def cat_verify(cats):
#     catBreed = [x['breed'] for x in cats]
#     catBreedCheck = map(lambda x: x == catBreed[0], catBreed)     
#     return all(catBreedCheck)

# cat_list = [
#     {
#         "name": "Lenny",
#         "breed": "Ragdoll",
#         "adopted": False
#     },
#     {
#         "name": "Roger",
#         "breed": "Siamese",
#         "adopted": False
#     },
#     {
#         "name": "Katya",
#         "breed": "Persian",
#         "adopted": True
#     }
# ]

# print(cat_verify(cat_list))    # False



cards = [
    {
        "company": "Wells Fargo",
        "card_name": "Active Cash",
        "annual_fee": 0,
        "intro_reward_type": "cash",
        "intro_reward_amount": 200,
        "num_users": 20
    },
    {
        "company": "Chase",
        "card_name": "Sapphire Preferred",
        "annual_fee": 95,
        "intro_reward_type": "points",
        "intro_reward_amount": 60000,
        "num_users": 54
    },
    {
        "company": "Citi",
        "card_name": "Diamond Preferred",
        "annual_fee": 0,
        "intro_reward_type": "cash",
        "intro_reward_amount": 150,
        "num_users": 13
    }
]

# Write your code here.

def sort_cards(card_list):
    return sorted(card_list, key=lambda x: x['num_users'], reverse=True)


print(sort_cards(cards))        # Chase, Wells Fargo, Citi


def sort_teachers_by_classroom_capacity(card_list):
    return [x['name'] for x in sorted(card_list, key=lambda x: x['classroom']['capacity'])]