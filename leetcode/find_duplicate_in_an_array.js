// https://leetcode.com/problems/find-all-duplicates-in-an-array/
// 442. Find All Duplicates in an Array
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function (nums) {
    let dups = [];
    for (let i = 0; i < nums.length; i++) {
        let index = Math.abs(nums[i]) -1
        if (nums[index] < 0) {
            dups.push(Math.abs(nums[i]))
        } else {
            nums[index] = -1 * Math.abs(nums[index])
        }
    }
    return dups;
}
function main() {
    let input = [2,2]
    let res = findDuplicates(input);
    console.log("here", res);

}
main();
