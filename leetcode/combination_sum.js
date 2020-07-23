// https://leetcode.com/problems/combination-sum/
/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */

var combinationSum = function(candidates, target) {
    let total = [];
    recursive([],0);
 
    function push(arr) {
        total.push(arr.slice())
    }
    function recursive(curr,index) {
        if (sum(curr) > target) {
            return null
        }
        else if (sum(curr) == target) {
            return curr
        }
        for (let i = index; i < candidates.length ; i++) {
            curr.push(candidates[i]);
            let res = recursive(curr,i);
            if (res) {
                push(res);
            }
            curr.pop()
        }
        return null
    }
    return total
};


function sum(arr) {
    return arr.reduce((a,num) => a+num ,0)
}
function main() {
    let candidates =[2,3,5,6];
    let target = 8;
    let res = combinationSum(candidates,target)
    console.log(res);

}

main()
