// https://leetcode.com/problems/maximum-product-of-word-lengths
// 318. Maximum Product of Word Lengths
/**
 * @param {string[]} words
 * @return {number}
 */
var maxProduct = function(words) {
    let bitMap = [];
    for (let i = 0; i < words.length; i++) {
        let word = words[i];
        for (let j = 0; j < word.length; j++) {
            // left shift by difference on position
            // eg left shift 'e' by 4(i.e. 101-97(charCode(a))
            // bitMap of abc = 7 (111) and ac=5 (101)
            bitMap[i] =  bitMap[i] | (1 << (word.charCodeAt(j) - 97));
        }
    }
    let max = 0;
    for (let i = 0; i < words.length; i++) {
        for (let j = i+1; j < words.length; j++) {
            if((bitMap[i] & bitMap[j]) === 0) {
                max = Math.max(max,words[i].length * words[j].length)
            }
        }

    }
    return max;
};

function main() {
    const words = ["abcw","baz","foo","bar","xtfn","abcdef"];
    const res = maxProduct(words)
    console.log(res);
}
main()
