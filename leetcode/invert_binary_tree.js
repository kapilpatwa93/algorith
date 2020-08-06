// https://leetcode.com/problems/invert-binary-tree/
// 226. Invert Binary Tree
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
 * @return {TreeNode}
 */
var invertTree = function(root) {
    return root ? invert(root) : root;

};

function invert(subRoot) {
    if (subRoot.left) {
        invert(subRoot.left)
    }
    if (subRoot.right) {
        invert(subRoot.right)
    }
    let temp = subRoot.left;
    subRoot.left = subRoot.right;
    subRoot.right = temp;
    return subRoot;
}
