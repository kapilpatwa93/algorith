// https://leetcode.com/problems/zigzag-conversion/submissions/
// 6. ZigZag Conversion
/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
   
    if (numRows == 1) {
        return s;
    }
    let str = [];
    for (let i = 0; i < numRows; i++) {
        let direction = -1 // -1 == down, 1 == up
        let num = 0;
        let prevNum = -1;
        while(num < s.length) {
            prevNum = num;
            if (direction === -1) {
                num = (num === 0 ? num : num+i) + i
                direction = 1;
            } else {
                num = num + (numRows-i)+(numRows-i-2)
                direction = -1;
            }
            if (num !== prevNum || num === 0) {
                str.push(s.charAt(num))
            }
        }
    }
    return str.join('');
};

function main() {
    let str = "ABCDE";
    let n = 2;
    let res = convert(str,n);
    console.log(res);
}
main()
