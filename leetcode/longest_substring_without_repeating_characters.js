// Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
    let map = new Map();
    let longest = 0;
    let count = 0;
    let lastIndex = 0;
    for (let i = 0; i < s.length; i++) {
        let char = s.charAt(i);
        let ex = map.get(char);
        if (ex != null && ex >= lastIndex) {
            longest = Math.max(longest,count);
            count = count - ((ex- lastIndex) + 1);
            lastIndex = ex + 1;
        }
        count++
        map.set(char,i);
    }
    if (longest < count) {
        longest = count;
    }
    return longest
};

function main() {
    let res = lengthOfLongestSubstring("abcabcbb")
    console.log(res);
}

main()
let i = 0;
console.log(i++)
console.log(i)
