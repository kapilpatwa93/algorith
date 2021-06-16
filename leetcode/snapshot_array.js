// https://leetcode.com/problems/snapshot-array/
// 1146. Snapshot Array
/**
 * @param {number} length
 */
let snapShots = [];
let snapCollection = {};
var SnapshotArray = function (length) {
    snapCollection = {};
    snapShots = [];
};

/**
 * @param {number} index
 * @param {number} val
 * @return {void}
 */
SnapshotArray.prototype.set = function (index, val) {
    snapCollection[index] = val;
};

/**
 * @return {number}
 */
SnapshotArray.prototype.snap = function () {
    snapShots.push(snapCollection);
    snapCollection = {};
    return snapShots.length - 1
};

/**
 * @param {number} index
 * @param {number} snap_id
 * @return {number}
 */
SnapshotArray.prototype.get = function (index, snap_id) {
    for (let i = snap_id; i >= 0; i--) {
        if (snapShots[i][index]) {
            return snapShots[i][index]
        }
    }
    return 0
};

function main() {
    const commands = ["SnapshotArray", "set", "snap", "set", "get"];
    const values = [[3], [0, 5], [], [0, 6], [0, 0]];
    const obj = new SnapshotArray(values[0]);
    let res = [null];
    for (let i = 1; i < commands.length; i++) {
        let val = obj[commands[i]](...values[i]);
        res.push(val === undefined ? null : val)
    }
    console.log(res);
}

main()
/**
 * Your SnapshotArray object will be instantiated and called as such:
 * var obj = new SnapshotArray(length)
 * obj.set(index,val)
 * var param_2 = obj.snap()
 * var param_3 = obj.get(index,snap_id)
 */
