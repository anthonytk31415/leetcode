def tree2str_helper(root):
    res = ''
    res = res + str(root.val)
    if not root.left and not root.right: 
        return res
    if root.left and root.right:
        res = res + '(' + tree2str_helper(root.left) + ')' + '(' + tree2str_helper(root.right) + ')'
    if root.left and not root.right: 
        res = res + '(' + tree2str_helper(root.left) + ')'
    if not root.left and root.right: 
        res = res + '()(' + tree2str_helper(root.right) + ')'
    return res