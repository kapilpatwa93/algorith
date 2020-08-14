// https://binarysearch.io/problems/Sum-of-right-leaves
// Sum of right leaves
/**
 * class Tree {
 *   constructor(val, left=null, right=null) {
 *     this.val = val
 *     this.left = left
 *     this.right = right
 *   }
 * }
 */
class Solution {
    solve(root) {
        return traverse(root, 0);
    }
}

function traverse(subRoot, sum) {
    if (!subRoot) {
        return sum
    }
    sum = traverse(subRoot.left, sum;
    if (subRoot.right && !subRoot.right.left && !subRoot.right.right) {
        sum += subRoot.right.val
    }
    sum = traverse(subRoot.right, sum)
    return sum
}

