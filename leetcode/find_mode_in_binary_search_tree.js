// https://leetcode.com/problems/find-mode-in-binary-search-tree/
// 501. Find Mode in Binary Search Tree (without using extra space)
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
 * @return {number[]}
 */
var findMode = function (root) {
    let ans = [];
    let prev = null;
    let maxCount = 1;
    let currentCount = 1;
    traverse(root, null);
    function traverse(root) {
        if (root == null) {
            return
        }
        traverse(root.left);
        if (prev === root.val && prev != null) {
            currentCount++;
        } else {
            currentCount = 1;
        }
        if (currentCount > maxCount) {
            ans = [prev];
            maxCount = currentCount;
        } else if (currentCount === maxCount) {
            ans.push(root.val);
        }
        prev = root.val;
        traverse(root.right);
    }

    return ans;
}


function main() {
    let input = [2, 1, 2, null, 1, null, 2, null, null, null, 1, null, null, null, null];
    let root = makeTree(input);
    let res = findMode(root);
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
