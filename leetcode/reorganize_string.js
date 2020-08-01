// https://leetcode.com/problems/reorganize-string/
// 767. Reorganize String
/**
 * @param {string} s
 * @return {string}
 */
var reorganizeString = function (s) {
    let frequencyMap = {};
    for (let i = 0; i < s.length; i++) {
        frequencyMap[s.charAt(i)] = ++frequencyMap[s.charAt(i)] || 1;
    }
    let arr = [];
    let maxSum = 0;
    for (const frequencyMapKey in frequencyMap) {
        maxSum = Math.max(maxSum, frequencyMap[frequencyMapKey])
        arr.push({
            char: frequencyMapKey,
            count: frequencyMap[frequencyMapKey]
        });
    }
    let remainingSum = s.length - maxSum;
    if (remainingSum >= maxSum - 1) {
        let strArr = [];
        let i = 0;
        while (i < s.length) {
            arr.sort((a, b) => parseInt(b.count) - parseInt(a.count));
            {
                let {char, count} = arr[0]
                if (count == 0) {
                    break;
                }
                strArr.push(char);
                --arr[0].count;
                i++
            }
            {
                let {char, count} = arr[1]
                if (count != 0) {
                    strArr.push(char);
                    --arr[1].count;
                    i++
                }
            }
        }
        return strArr.join("");
    }
    return "";
};

function main() {
    const s = "abaa";
    const res = reorganizeString(s);
    console.log("res", res);
}

main()
