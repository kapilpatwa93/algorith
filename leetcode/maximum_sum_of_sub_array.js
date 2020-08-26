function main() {
    let arr =[1,-10,3,5,-10,3,6];
    let res= solve(arr);
}
function solve(arr) {
    let sumArr = [arr[0]];
    for (let i = 1; i < arr.length; i++) {
        sumArr.push(sumArr[i-1] + arr[i])
    }
    console.log(sumArr);
    let min =0;
    let max = Number.NEGATIVE_INFINITY;
    // [ 1,-9,  -6, -1, -11, -8, -2 ]
    for (let i = 0; i < arr.length; i ++) {
        console.log(sumArr[i],min);
        max = Math.max(sumArr[i]-min,max);
        min = Math.min(min,sumArr[i])
    }
    console.log(max);
    // console.log(sumArr);
}
main()
// maximum subarray 
