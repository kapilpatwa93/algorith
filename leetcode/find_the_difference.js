// https://leetcode.com/problems/find-the-difference/
// 389. Find the Difference
/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function (s, t) {
    let mapS = new Map();
    let mapT = new Map();
    for (let i = 0; i < s.length; i++) {
        let count =  mapS.get(s.charAt(i));
        if(count) {
            count+=1
        } else {
            count = 1
        }
        mapS.set(s.charAt(i), count++);
    }
    for (let i = 0; i < t.length; i++) {
        let count =  mapT.get(t.charAt(i));
        if(count) {
            count+=1
        } else {
            count = 1
        }
        mapT.set(t.charAt(i), count)
    }
    let largerMap = mapS.size > mapT.size ? mapS : mapT;
    let smallerMap = mapS.size <= mapT.size ? mapS : mapT;
    let extra = '';
    largerMap.forEach((v,k) => {
        let count = smallerMap.get(k) || 0
        if(v-count  >= 1) {
            extra = k
        }
    })
    return extra
};

function main() {
    let s ="abcd";
    let t ="abcde";
    let res = findTheDifference(s,t);
    console.log(res);
}

main()
