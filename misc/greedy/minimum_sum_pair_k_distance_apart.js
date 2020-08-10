// https://www.geeksforgeeks.org/minimum-sum-of-a-pair-at-least-k-distance-apart-from-an-array/
/**
 * @param {number[]} arr
 * @param {number} distance
 * @return {number}
 */
function minimum_pair(arr, distance) {
    let suffixArr = new Array(arr.length);
    suffixArr[arr.length-1] = arr[arr.length-1]
    for (let i = arr.length-2; i >= 0; i--) {
        suffixArr[i] = Math.min(suffixArr[i+1],arr[i])
    }
    let minSum = Number.POSITIVE_INFINITY;
    for (let i = 0; i < arr.length-(distance); i++) {
        minSum = Math.min(minSum,arr[i]+suffixArr[i+(distance)])
    }
    console.log(minSum);
    console.log(suffixArr);

}

function main() {
    // let arr = [1, 2, 3, 4, 5, 6];
    // let arr = [4, 2, 5, 4, 3, 2, 5];
    let arr = [4,2,3,1,2,3,6];
    let distance = 4;
    minimum_pair(arr,distance);
}
main();
