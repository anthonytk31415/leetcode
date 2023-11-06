


function TreeNode(val, left, right) {
     this.val = (val===undefined ? 0 : val)
     this.left = (left===undefined ? null : left)
     this.right = (right===undefined ? null : right)
}


// var sumOfLeftLeaves = function(root) {
//     let res = []
//     if (!root) {
        
//     } else {

//     }
// }



var inordertraversal = function(root) {
    let res = []
    if (!root) {
        return res;
    } else {
        res = res.concat(inordertraversal(root.left))
        res.push(root.val)
        res = res.concat(inordertraversal(root.right))
        return res
    }
}

// const root = new TreeNode(3)
// root.left = new TreeNode(9)
// root.right = new TreeNode(20)
// root.right.left = new TreeNode(15)
// root.right.right = new TreeNode(7)


const root = new TreeNode(10)
root.left = new TreeNode(5)
root.right = new TreeNode(20)
root.right.left = new TreeNode(15)
root.right.right = new TreeNode(22)

console.log(inordertraversal(root))