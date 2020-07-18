// https://binarysearch.io/problems/Space-Battle
// Space Battle
class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    solve(nums) {
        let i = 0;
        let max = 0;
        let temp = [];
        let all = [];
        while(i < nums.length) {
            let curr = nums[i];
            if (curr < 0) {
                while(temp[temp.length -1] < Math.abs(curr)) {
                    temp.pop()
                }
                if (temp[temp.length -1] == Math.abs(curr)) {
                    temp.pop();
                } else if (temp.length == 0) {
                    all.push(curr)
                }

            } else  {
                max = Math.max(curr,max);
                temp.push(curr);
            }
            i++;
        }
        all.push(...temp);
        return all;
    }
}

function main() {
    let nums =[1, 5, 3, -6, 7];
    let res = new Solution().solve(nums);
    console.log(res);
}
main()
