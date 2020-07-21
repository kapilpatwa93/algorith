// https://binarysearch.io/problems/Split-List
// Split List
class Solution {
    solve(nums) {
        let n = nums.length;
        let maxPrefixArray = new Array(n);
        let minSuffixArray = new Array(n);
        maxPrefixArray[0] = nums[0];
        minSuffixArray[n - 1] = nums[n - 1];
        // calculating max prefix array
        for (let i = 1; i < n; i++) {
            maxPrefixArray[i] = Math.max(maxPrefixArray[i - 1], nums[i]);
        }
        // calculating min suffix array
        for (let i = n - 2; i >= 0; i--) {
            minSuffixArray[i] = Math.min(minSuffixArray[i + 1], nums[i]);
        }
        for (let i = 0; i < n - 1; i++) {
            if (maxPrefixArray[i] < minSuffixArray[i + 1]) {
                return true;
            }
        }
        return false;
    }

}

function main() {
    let nums = [7, 8, 9, 9];
    let res = new Solution().solve(nums);
    console.log(res);
}

main()
