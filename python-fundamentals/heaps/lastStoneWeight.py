# lastStoneWeight


def lastStoneWeight(stones):
    if len(stones) == 0:
        return 0
    elif len(stones) == 1:
        return stones[0]
    stones = sorted(stones)
    largest, nextLargest = stones[-1], stones[-2]
    if largest == nextLargest: 
        return lastStoneWeight(stones[:-2])
    else: 
        return lastStoneWeight(stones[:-2] + [largest - nextLargest])


stones = [148, 76, 87, 102, 35 , 38]
print(lastStoneWeight(stones))