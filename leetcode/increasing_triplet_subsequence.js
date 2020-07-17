// https://leetcode.com/problems/increasing-triplet-subsequence/
// Increasing Triplet Subsequence

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var increasingTriplet = function (nums) {
    let n1 = Number.POSITIVE_INFINITY;
    let n2 = Number.POSITIVE_INFINITY;
    let isValid = false;
    for (let i = 0; i < nums.length; i++) {
        if(nums[i] < n1) {
            n1 = nums[i]
        } else if (nums[i] > n1 && nums[i] < n2) {
            n2 = nums[i];
        } 
        else if (n1 < n2 && n2 < nums[i]) {
            isValid = true;
            break;
        }
        
    }
    return isValid
};


function main() {
    let nums = [1,1,-2,6];
    let res = increasingTriplet(nums);
    console.log(res);
}

main()
