// https://binarysearch.io/problems/Rocketship-Rescue
class Solution {
    /**
     * @param {number[]} weights
     * @param {number} limit
     * @return {number}
     */
    solve(weights, limit) {
        weights.sort((a,b) => parseInt(a)-parseInt(b));
        let i =0;
        let count = 0;
        let j = weights.length -1;
        while(i <= j) {
            if(weights[i]+weights[j] <= limit) {
                i++;
                j--;
            } else {
                j--;
            }
            count++
        }
        return count;
    }
}
function main() {
    let numbers = [200,300,200];
    let limit = 300;
    let res = new Solution().solve(numbers,limit);
    console.log(res);
}

main();
