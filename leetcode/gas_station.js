// https://leetcode.com/problems/gas-station/
// 134. Gas Station
/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */

var canCompleteCircuit = function (gas, cost) {
    for (let i = 0; i < gas.length; i++) {
        let count = 0;
        let startIndex = i;
        let pointer = startIndex;
        let prevCost = 0;
        let fuel = 0;
        while (count <= gas.length) {
            if (pointer === gas.length) {
                pointer = 0;
            }
            fuel = fuel - prevCost + gas[pointer];

            prevCost = cost[pointer]
            if (fuel < prevCost) {
                startIndex = -1;
                break;
            }
            count++;
            pointer++;
        }
        if (startIndex !== -1) {
            return startIndex
        }
    }
    return -1
};

function main() {
    const gas = [1, 2, 3, 4, 5]
    const cost = [3, 4, 5, 1, 2]
    let res = canCompleteCircuit(gas, cost);
    console.log(res);
}

main()
