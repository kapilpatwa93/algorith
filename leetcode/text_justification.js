// https://leetcode.com/problems/text-justification/
// 68. Text Justification
/**
 * @param {string[]} words
 * @param {number} maxWidth
 * @return {string[]}
 */
var fullJustify = function (words, maxWidth) {
    let sentences = [];
    let count = 0;
    while (count < words.length) {
        let len = 0;
        let requiredWords = [];
        while (len < maxWidth && count < words.length) {
            let wordLen = words[count].length;
            if (canFit(len, wordLen, maxWidth)) {
                requiredWords.push(words[count])
                count++;
                len = len + wordLen + 1
            } else {
                break;
            }
        }
        len--;
        sentences.push(formSentence(requiredWords, count == words.length, maxWidth))
    }
    return sentences
};

function canFit(curr, wordLength, maxWidth) {
    return curr + wordLength <= maxWidth
}

function formSentence(arr, isLast, maxWidth) {
    let strLen = arr.join('').length
    let div = !isLast ? parseInt((maxWidth - strLen) / (arr.length - 1)): 1
    let mod = !isLast ? (maxWidth - strLen) % (arr.length - 1): 0;
    let str = ''
    for (let i = 0; i < arr.length - 1; i++) {
        str += arr[i] + getNSpace(div + (i < mod ? 1 : 0))
    }
    str += arr[arr.length-1] + getNSpace(maxWidth-(str.length + arr[arr.length-1].length))
    return str
}
function getNSpace(n) {
    let spaces = ''
    for (let i = 0; i < n; i++) {
        spaces += ' '
    }
    return spaces;
}
function main() {
    let words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
    let maxWidth = 14;
    let res = fullJustify(words, maxWidth);
    console.log(res);
}

main()
