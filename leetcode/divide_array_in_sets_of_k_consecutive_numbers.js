// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
// 1296. Divide Array in Sets of K Consecutive Numbers
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var isPossibleDivide = function (nums, k) {
    let map = {};
    for (let i = 0; i < nums.length; i++) {
        map[nums[i]] = ++map[nums[i]] || 1
    }
    let sortedSet = Array.from(new Set(nums)).sort((a, b) => parseInt(a) - parseInt(b));
    let i = 0;
    let pointer = 0;
    let flag = true;
    outer:while (pointer < sortedSet.length) {
        let start = sortedSet[pointer];
        if (!map[start]) {
            pointer++;
            continue;
        }
        for (let j = 0; j < k; j++) {
            if (map[start] >= 1) {
                map[start] -= 1;
            } else {
                flag = false;
                break outer;
            }
            start++;
            i++;
        }
    }
    return flag;
};

function main() {
    let nums = [1, 2, 3, 4, 2, 3, 4, 5, 3, 4, 5, 6];
    let k = 4;
    let res = isPossibleDivide(nums, k);
    console.log(res);
}

main()
