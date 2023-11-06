
# get to median, then for the left and right, call

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedListToBST(head):
    def helper(head):
        if not head: 
            return None
        head_len = 0
        node = head

        while node: 
            node = node.next
            head_len +=1
        
        if head_len <= 1:
            return TreeNode(head.val)

        left_list = head
        median = head
        med_prev = None
        for _ in range(head_len//2):
            med_prev = median
            median = median.next

        if med_prev:
            med_prev.next = None
        right_list = median.next

        tree_root = TreeNode(median.val)
        tree_root.left = helper(left_list)
        tree_root.right = helper(right_list)
        
        return tree_root
    return helper(head)




def build_list(arr):
    dummy = ListNode()
    node = dummy
    for x in arr: 
        node.next = ListNode(x)
        node = node.next
    return dummy.next

arr = [-10,-3,0,5,9]


def print_list(lst):
    node = lst
    while node: 
        print(node.val)
        node = node.next


# print_list(build_list(arr))

x = sortedListToBST(build_list(arr))


def inorder(root):
    res = []
    if not root: 
        return res  
    else: 
        res = res + inorder(root.left)
        res.append(root.val)
        return res + inorder(root.right)

print(inorder(x))