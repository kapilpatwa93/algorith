// https://leetcode.com/problems/house-robber/
// 198. House Robber
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
    let prev = 0, cur = 0;
    for (let n of nums) {
        let temp = cur;
        cur = Math.max(prev + n, cur);
        prev = temp;
    }
    return Math.max(cur, prev);
}


function main() {
    let nums = [2, 7, 9, 15, 1];
    let res = rob(nums);
    console.log(res);
}

main()
