/**
 * @param {number[][]} trips
 * @param {number} capacity
 * @return {boolean}
 */
var carPooling = function (trips, capacity) {
    let capacityArr = new Array(1001).fill(0)
    let maxTo = 0
    for (let i = 0; i < trips.length; i++) {
        let cap = trips[i][0]
        let to = trips[i][1]
        let from = trips[i][2]
        capacityArr[to] = capacityArr[to] + cap
        if (from < 1000) {
            capacityArr[from] = capacityArr[from] - cap
        }
        maxTo = Math.max(maxTo, from)
    }

    let total = 0;
    let limit = Math.min(maxTo, capacityArr.length)
    for (let i = 0; i < limit; i++) {
        capacityArr[i] = capacityArr[i] + total
        total = capacityArr[i]
        if (total > capacity) {
            return false
        }
    }
    return true
};

function main() {
    let trips = [[2, 1, 5], [3, 3, 7]]
    let capacity = 4
    let res = carPooling(trips, capacity)
    console.log(res);
}

main()