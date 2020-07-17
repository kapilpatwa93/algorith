// https://leetcode.com/problems/next-greater-element-i/
// 496. Next Greater Element I
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function (nums1, nums2) {
    let map = new Map();
    let stack = [];
    for (let i = 0; i < nums2.length; i++) {
        while (stack[stack.length - 1] < nums2[i]) {
            map.set(stack.pop(), nums2[i]);
        }
        stack.push(nums2[i])
    }
    let arr = [];
    for (let i = 0; i < nums1.length; i++) {
        arr.push(map.get(nums1[i]) || -1)
    }
    return arr;
};

function main() {
    let nums1 = [1, 3, 5, 2, 4]
    let nums2 = [6, 5, 4, 3, 2, 1, 7];
    let res = nextGreaterElement(nums1, nums2);
    console.log(res);
}
main()

