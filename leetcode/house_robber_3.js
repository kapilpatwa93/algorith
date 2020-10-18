// https://leetcode.com/problems/house-robber-iii/
// 337. House Robber III
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */

var rob = function (root) {
    return Math.max(...recurse(root));
};

function recurse(root) {
    let res = new Array(2).fill(0);
    if (!root) {
        return res
    }
    let left = recurse(root.left);
    let right = recurse(root.right);
    res[0] = root.val + left[1] + right[1];
    res[1] = Math.max(...left) + Math.max(...right)
    return res;
}

function main() {
    let arr = [2, 3, 5, 6, 10, 6, 9, 3, 7, 6, 3, 7, 3, 3, 2];
    let root = makeTree(arr);
    let res = rob(root)
    console.log(res);
}

main();

// --- helper function for tree 
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

function makeTree(input) {
    function getTree(subRootIndex) {
        if (subRootIndex >= input.length || input[subRootIndex] == null) {
            return null
        }
        return new TreeNode(input[subRootIndex], getTree((subRootIndex * 2) + 1), getTree((subRootIndex + 1) * 2))
    }
    return getTree(0)
}
