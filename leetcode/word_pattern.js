// https://leetcode.com/problems/word-pattern/
// 290. Word Pattern
/**
 * @param {string} pattern
 * @param {string} str
 * @return {boolean}
 */
var wordPattern = function (pattern, str) {
    let strArr = str.split(" ");
    let map = {};
    let revMap = {};
    if (pattern.length != strArr.length) {
        return false
    }
    let res = true;
    for (let i = 0; i < pattern.length; i++) {
        if ((map[pattern.charAt(i)] && map[pattern.charAt(i)] !== strArr[i]) || (revMap[strArr[i]] && revMap[strArr[i]] !== pattern.charAt(i))) {
            res = false;
            break;
        } else {
            map[pattern.charAt(i)] = strArr[i];
            revMap[strArr[i]] = pattern.charAt(i);
        }
    }
    return res;

};

function main() {
    let pattern = "abba";
    let string = "dog ca ca dog"
    let res = wordPattern(pattern, string);
    console.log(res);
}

main();
