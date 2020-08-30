// https://leetcode.com/problems/partition-equal-subset-sum/
// 416. Partition Equal Subset Sum
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function (nums) {
    let total = nums.reduce((sum, a) => sum + a, 0);
    let half = total / 2;
    if (total != Math.floor(half) * 2) {
        return false;
    }
    return recurse(nums, 0, half);

    function recurse(nums, index, total) {
        if (total == 0) {
            return true;
        }
        if (total < 0 || index == nums.length) {
            return false
        }
        if (recurse(nums, index + 1, total - nums[index])) {
            return true
        }
        let j = index + 1;
        while (j <= nums.length && nums[index] == nums[j]) {
            j++;
        }
        return recurse(nums, j, total)
    }
};

function main() {
    let arr = [1, 2, 2, 3, 3, 3];
    let res = canPartition(arr);
    console.log(res);
}

main();
