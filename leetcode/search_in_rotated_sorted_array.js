// https://leetcode.com/problems/search-in-rotated-sorted-array/
// 33. Search in Rotated Sorted Array
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
    let left = 0;
    let right = nums.length - 1;
    while (left <= right) {
        let mid = parseInt((left + right) / 2);
        let midNum = nums[mid];
        let lNum = nums[left];
        let rNum = nums[right];
        if (target == midNum) {
            return mid;
        } else if (target == rNum) { // optional check to optimize runtime
            return right;
        } else if (target == lNum) { // optional check to optimize runtime
            return left;
        }
        if (target > midNum && target > rNum && midNum <= rNum) {
            right = mid - 1;
        } else if (target > midNum) {
            left = mid + 1
        } else if (target < midNum && target < lNum && midNum >= lNum) {
            left = mid + 1
        } else if (target < midNum) {
            right = mid - 1;
        }
    }
    return -1

};

function main() {
    let nums = [6, 7, 8, 1, 2, 3, 4, 5];
    let target = 1;
    let res = search(nums, target);
    console.log(res);
}
main()
