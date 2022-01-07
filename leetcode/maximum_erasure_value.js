/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumUniqueSubarray = function(nums) {
    let prefixSum = new Array(nums.length);

    let posMap = {}
    prefixSum[0] = nums[0]
    for (let i = 1; i < nums.length;i++) {
        prefixSum[i] = nums[i] + prefixSum[i-1]
    }

    let p1 = 0
    let p2 = 0
    let m = 0
    while (p1 < nums.length && p2 < nums.length){
        let num = nums[p2]
        if (posMap[num] != undefined && posMap[num] >= 0) {
            m = Math.max(prefixSum[p2-1]-prefixSum[p1]+nums[p1], m)
            if (p1 < posMap[num]+1) {
                p1 = posMap[num]+1
            }

        }
        posMap[num] = p2
        p2++
    }
    m = Math.max(prefixSum[p2-1]-prefixSum[p1]+nums[p1], m)
    return m
};

function main() {
    let nums = [5,2,1,2,5,2,1,2,5]
    let res = maximumUniqueSubarray(nums)
    console.log(res);
}
main()