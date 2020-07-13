// https://leetcode.com/problems/count-and-say/
// 38. Count and Say

/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function (n) {
    let str = "1";
    for (let i = 1; i < n; i++) {
        str = parseStr(str)
    }
    return str;
};
function parseStr(str) {
    let count = 1;
    let prev = str.charAt(0);
    let parsedStr = '';
    for (let i = 1; i < str.length; i++) {
        if(prev == str.charAt(i)) {
            count ++
        } else {
            parsedStr += `${count}${prev}`
            count = 1;
        }
        prev = str.charAt(i);
    }
    parsedStr += `${count}${prev}`
    return parsedStr
}
function main() {
    let n = 5;
    let res = countAndSay(n);
    console.log(res);
}

main()
