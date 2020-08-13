// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
// Element Appearing More Than 25% In Sorted Array  
/**
 * @param {number[]} arr
 * @return {number}
 */
var findSpecialInteger = function(arr) {
    let prevNum = arr[0];
    let count = 1;
    let maxCount = 1;
    let maxCountNum = arr[0];
    for (let i = 1; i < arr.length; i++) {
        if (prevNum === arr[i]) {
            count++
        } else {
            count = 1
        }
        prevNum = arr[i];
        if(count > maxCount) {
            maxCount = count;
            maxCountNum = arr[i];
        }
    }
    return maxCountNum;
};

function main() {
    let arr = [1,2,2,6,6,6,6,7,10];
    let res = findSpecialInteger(arr);
    console.log(res);
}

main();
