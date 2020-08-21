// https://leetcode.com/problems/non-overlapping-intervals/
// 435. Non-overlapping Intervals

/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function(intervals) {
    intervals.sort((a,b) => parseInt(a[1])-parseInt(b[1]));
    let count = 0;
    let prev = 0;
    let next = 1;
    while(next < intervals.length) {
        if(intervals[prev][1] > intervals[next][0]) {
            count++
        } else {
            prev = next;
        }
        next++;
    }
    return count;
};

function main() {
    let intervals = [[1,2],[2,3],[1,3],[3,6],[3,4],[4,5], [6,7],[7,8],[8,9]];
    let res = eraseOverlapIntervals(intervals);
    console.log(res);
}
main();
