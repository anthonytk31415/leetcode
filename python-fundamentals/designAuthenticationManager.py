# do you need a dicionary to keep track of whether the token has expired? 
# 

from collections import OrderedDict
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = OrderedDict()   ## self.tokens[token] = {start: curTime, expiration: curTime + timeToLive}; only keep track of live tokens; will be deleted 

    def generate(self, tokenId: str, currentTime: int):
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int):
        if tokenId in self.tokens: 
            if currentTime < self.tokens[tokenId]:
                del self.tokens[tokenId]
                self.tokens[tokenId] = currentTime + self.timeToLive
        else: 
            return 

    def countUnexpiredTokens(self, currentTime: int):
        counter = 0 
        for token in self.tokens: 

            if currentTime < self.tokens[token]:
                break
            else: 
                del self.tokens[token]
        return len(self.tokens)