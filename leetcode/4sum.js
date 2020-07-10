// https://leetcode.com/problems/4sum/
// 18. 4Sum
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    nums.sort((a, b) => parseInt(a) - parseInt(b));
    let map = {};
    let res = [];

    function add(a, b, c, d) {
        if (map[`${a}${b}${c}${d}`] === undefined) {
            res.push([a, b, c, d])
            map[`${a}${b}${c}${d}`] = 1
        }
    }

    function total(a, b, c, d) {
        return a + b + c + d
    }

    for (let i = 0; i < nums.length - 3; i++) {
        for (let j = i + 1; j < nums.length - 2; j++) {
            let k = j + 1
            let l = nums.length - 1;
            while (k < l) {
                let s = total(nums[i], nums[j], nums[k], nums[l])
                if (s == target) {
                    add(nums[i], nums[j], nums[k], nums[l]);
                    // console.log(arr[i],arr[j],arr[k],arr[l]);
                    k++;
                    l--;
                } else if (s < target) {
                    k++
                } else {
                    l--
                }
            }
        }
    }
    // console.log(map);
    return res;
}

function main() {
    let arr = [1, 0, -1, 0, -2, 2];
    let sum = 0;
    let res = fourSum(arr, sum);
    console.log(res);
}
main()
