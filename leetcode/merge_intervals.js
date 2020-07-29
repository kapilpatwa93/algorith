// https://leetcode.com/problems/merge-intervals/
// 56. Merge Intervals
/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
    intervals.sort((a, b) => parseInt(a[0]) - parseInt(b[0]));
    let i = 0;
    let arr = [];
    for (i = 0; i < intervals.length; i++) {
        let start = i;
        let min = intervals[start][0];
        let max = intervals[start][1]
        while (i < intervals.length - 1) {
            if (max >= intervals[i + 1][0]) {
                min = Math.min(min, intervals[i + 1][0])
                max = Math.max(max, intervals[i + 1][1])
                i++
            } else {
                break;
            }
        }
        arr.push([min, max])
    }
    return arr;
};
