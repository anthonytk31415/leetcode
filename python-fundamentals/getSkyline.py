
# Group into overlapping x values, sorted by height 
# - create array of max heaps; once you get something nonoverlapping, create a new heap and store it in an array

# then for each heap: ** need to thinka bout U shaped patterns
    
# - the top one defines the x1, x2
# - then the next one takes the x1, x2 that does not overlap the previous x1-x2; 
#     - create a new combined previous x1-x2
# - do that loop
# - when you get to the end of the current heap, add at the end the max combined x2 with 0

# - for each segment, append the segment in a res = min heap





# time: 
# - create heap: n1(logn1)
# - extract from heap: n 
# --> nlogn
# space: o(n) for the intermediate heap

from heapq import heappush, heappop
from math import inf

def getSkyline(buildings):

    overlap = []
    cur_heap = []
    left, right, height = buildings[0]
    heappush(cur_heap, (-height, left, right))
    curMLeft, curMRight = left, right
    for i in range(1, len(buildings)):
        left, right, height = buildings[i]
        if max(right, curMRight) - min(left, curMLeft) <= (right - left) + (curMRight - curMLeft):   ## ranges overlap
            heappush(cur_heap, (-height, left, right))
            curMLeft = max(curMLeft, left)
            curMRight = min(curMRight, right)
        else: 
            overlap.append(cur_heap)
            cur_heap = []
            heappush(cur_heap, (-height, left, right))
            curMLeft, curMright = left, right
    overlap.append(cur_heap)

    print(overlap)

    res = []

    #mabe we need to biuld this with intervals

    # now build the line segments
    for heap in overlap: 
        segments = []           # keep the segments in order of their left 
        right_max = -inf
        while heap: 
            ht_cur, le_cur, ri_cur = heappop()      ## cur is being compared to the segments seg
            right_max = max(right_max, ri_cur)
            if not segments: 
                heappush(segments, [le_cur, ri_cur, ht_cur])
            else: 
                add_to_seg = []
                for le_seg, ri_seg, ht_seg in segments:
                    if ri_cur - le_cur <= 0: 
                        break
                    if ri_cur <= le_seg:
                        heappush(add_to_seg, [le_cur, ri_cur, ht_cur]) 
                        le_cur, ri_cur = 0, 0
                        break
                    elif le_seg <= ri_cur:
                        heappush(add_to_seg, [le_cur, le_seg, ht_cur])
                        if ri_cur <= ri_seg:
                            le_cur, ri_cur = 0, 0
                            break
                        else: 
                            le_cur = ri_seg
                    elif le_seg > ri_cur:
                        ri_cur = max(, ) 
                        continue

                if ri_cur - le_cur > 0: 
                    heappush(add_to_seg, [le_cur, ri_cur, ht_cur]) 
        


    print(res)
    return res

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
getSkyline(buildings)
