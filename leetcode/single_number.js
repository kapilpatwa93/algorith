// https://leetcode.com/problems/single-number/
// 136. Single Number
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
    let a = 0;
    for (let i = 0; i < nums.length; i++) {
        a ^= nums[i]
    }
    return a
};
function main() {
    let nums = [1,2,1,3,4,2,4]
    let res = singleNumber(nums)
    console.log(res);
}
main()
