// https://leetcode.com/problems/subsets-ii/submissions/
// 90. Subsets II
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function (nums) {
    nums.sort((a, b) => parseInt(a) - parseInt(b))
    let res = [];
    let map = {};
    recurse(nums, 0, []);
    res.push([])
    for (const mapKey in map) {
        res.push(map[mapKey])
    }
    return res;
    function recurse(nums, start, arr) {
        if (start < nums.length) {
            for (let i = start; i < nums.length; i++) {
                let nArr = arr.slice();
                nArr.push(nums[i]);
                map[nArr.join("")] = nArr
                recurse(nums, i + 1, nArr)
            }
        }
    }
};

function main() {
    let arr = [1, 2, 2];
    let res = subsetsWithDup(arr);
    console.log(res);
}

main();
