# MLE for having too many arrays: first iteration had 1 array per snap



#################################
# 2nd iteration: linkedlist; TLE


# class ListNode: 
#     def __init__(self, snap_id, val):
#         self.snap_id = snap_id
#         self.val = val
#         self.next = None

# class SnapshotArray:

#     def __init__(self, length: int):
#         self.length = length
#         self.arr = [0 for _ in range(self.length)]
#         self.snaps = [ListNode(-1, 0) for _ in range(self.length)]
#         self.snapCalls = 0

#     def set(self, index: int, val: int) -> None:
#         self.arr[index] = val        

#     def snap(self) -> int:
#         self.snapCalls += 1
#         snap_id = self.snapCalls -1 
#         for i in range(len(self.arr)):
#             if self.arr[i] != self.snaps[i].val: 
#                 newNode = ListNode(snap_id, self.arr[i])
#                 newNode.next = self.snaps[i]
#                 self.snaps[i] = newNode

#         return snap_id

#     def get(self, index: int, snap_id: int) -> int:
#         node = self.snaps[index]        
#         while node: 
#             if node.snap_id <= snap_id:
#                 return node.val
#             node = node.next


#################################
# 3rd iteration: binary search


# class Node:
#     def __init__(self):
#         self.snap_id_tracker = [-1]
#         self.values = {-1: 0}

from collections import defaultdict
class SnapshotArray:

    # at the end of the snaps will be the latest snap
    # the corresponding index of that snap in snap_id_tracker is the value 
    def __init__(self, length: int):
        self.length = length
        self.data = defaultdict(list)
        self.snapCalls = 0

    def set(self, index: int, val: int) -> None:
        if self.data[index] and self.data[index][-1][0] == self.snapCalls:
            self.data[index][-1][1] = val
            return 
        self.data[index].append([self.snapCalls, val])

    def snap(self) -> int:
        self.snapCalls += 1
        return self.snapCalls - 1

    # binSearch: if the number equals snap_id, return the index; 
    # else return the largest one smaller than the snap id
    # - Assume arr is sorted. 
    def binSearch(self, arr, snap_id):
        left, right = 0, len(arr) - 1
        while left <= right:
            if left == right: 
                if arr[left][0] <= snap_id: 
                    return left
                else:
                    return left - 1
            mid = (left + right) // 2
            if arr[mid][0] == snap_id: 
                return mid
            if arr[mid][0] > snap_id:
                right = mid - 1 
            else: 
                left = mid + 1
        return right

    def get(self, index: int, snap_id: int) -> int:
        node = self.data[index]
        pos = self.binSearch(node, snap_id)
        if pos == -1:
            return 0
        else: 
            return node[pos][1]            





z = SnapshotArray(1)
z.set(0,15)
# print(z.arr)

# print(z.snaps)

z.snap()


z.snap()
z.snap()

# print(z.snaps[0].snap_id_tracker)
# print(z.snaps[0].values)

# print(z.binSearch([-1, 0], 2))
print(z.get(0,2))