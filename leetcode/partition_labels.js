// https://leetcode.com/problems/partition-labels/
// 763. Partition Labels
/**
 * @param {string} s
 * @return {number[]}
 */
var partitionLabels = function(s) {
    let occMap = {};
    for (let i = 0; i < s.length; i++) {
        let c = s.charAt(i);
        if(occMap[c]) {
            occMap[c][1] = i;
        }else {
            occMap[c] = [i,i]
        }
    }
    let intervals = [];
    for (const occMapKey in occMap) {
        intervals.push(occMap[occMapKey])
    }
    intervals.sort((a1,a2) => {
        return  a1[0]- a2[0]
    })
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
    return arr.map(a=> a[1]-a[0] + 1)
};
function main() {
    let s = "ababcbacadefegdehijhklij"
    let res = partitionLabels(s);
    console.log(res);

}
main()
