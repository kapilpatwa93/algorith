// https://binarysearch.io/problems/coco-kaka
// Coco Kaka
class Solution {
    solve(s, t) {
        const map1 = {}
        const map2 = {}
        if (s.length !== t.length) {
            return false;
        }
        for (let i = 0; i < s.length; i++) {
            if (map1[s.charAt(i)] && map1[s.charAt(i)] !== t.charAt(i)) {
                return false;
            } else {
                map1[s.charAt(i)] = t.charAt(i);
            }
            if (map2[t.charAt(i)] && map2[t.charAt(i)] !== s.charAt(i)) {
                return false;
            } else {
                map2[t.charAt(i)] = s.charAt(i);
            }
        }
        return true;
    }
}

function main() {
    const s = "abc";
    const t = "pqr";
    const res = new Solution().solve(s,t);
    console.log(res);
}
main()
