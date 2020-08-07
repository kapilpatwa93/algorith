// https://leetcode.com/problems/binary-tree-right-side-view/
// 199. Binary Tree Right Side View
/**
 * @param {TreeNode} root
 * @return {number[]}
 */

var rightSideView = function (root) {
    let map = {};
    traverse(root, 0);
    let keys = Object.keys(map);
    let res = new Array(keys.length);
    for (let i = 0; i < keys.length; i++) {
        res[keys[i]] = map[keys[i]]
    }
    function traverse(root, depth) {
        if (!root) {
            return;
        }
        traverse(root.left, depth + 1);
        traverse(root.right, depth + 1);
        map[depth] = root.val;
    }

    return res;
};

function main() {
    let input =[1,2,3,4,5,6,null,8,9,10,null,12,13,14,15]
    let root = makeTree(input);
    let res = rightSideView(root);
    console.log(res);

}

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

main();
