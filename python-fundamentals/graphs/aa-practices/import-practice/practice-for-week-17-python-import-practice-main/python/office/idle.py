
# Your code here

from math import floor
from random import random

def chat ():
    coworkers = ["Jack", "Lenny", "Michelle", "Andrea"]
    chatee = coworkers[floor(random()*4)]
    print(f'Chatting with {chatee}...')
    print('Done')


def getWater():
    print('Getting water...')
    print('That was refreshing.')

def useSocialMedia():
    socialMedia = ["FaceBook", "Twitter", "YouTube", "Reddit"]
    choice = socialMedia[floor(random()*4)]
    print(f'Using {choice}...')
    print('Done')