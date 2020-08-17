// https://binarysearch.io/problems/Largest-Sum-of-Non-Adjacent-Numbers
// Largest Sum of Non-Adjacent Numbers
class Solution {
    solve(nums) {
        let res = [0, 0];
        for (let i = 0; i < nums.length; i++) {
            let curr = nums[i] + res[1];
            res[1] = Math.max(res[0], res[1])
            res[0] = curr
        }
        return Math.max(...res)
    }
}

function main() {
    let nums = [1, 2, 3, 4, 6, 9, 6, 3]
    let res = new Solution().solve(nums);
    console.log(res);
}
main()
