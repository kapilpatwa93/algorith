//https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
// 1218. Longest Arithmetic Subsequence of Given Difference
/**
 * @param {number[]} arr
 * @param {number} difference
 * @return {number}
 */
var longestSubsequence = function(arr, difference) {
    let map = new Map();
    for (let i = 0; i < arr.length; i++) {
        let entry = map.get(arr[i] - difference);
        map.set(arr[i], entry !== undefined? entry + 1: 1)
    }
    return Math.max(...map.values())
   
};
function main() {
    let arr =  [1,2,3,4,6,4,5,6,3,6,7,2,6,8,9,10];
    let diff = 1;
    let res = longestSubsequence(arr,diff);
    console.log(res);
}
main();
