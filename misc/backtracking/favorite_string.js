/**
 * @return {number} spaces
 * @param {string} str
 * @param {[string]}favourites
 */
function backTrackingApproach(str, favourites) {
    let counts = [];
    recursiveFn(str, favourites, 0, 0);

    function recursiveFn(str, favourites, pos, count) {
        if (pos == str.length) {
            return {
                pos: pos,
                count: count
            }
        }
        for (let i = 0; i < favourites.length; i++) {
            let currStr = favourites[i];
            let len = currStr.length - 1;
            if (str.charAt(pos) == currStr.charAt(0) && str.charAt(pos + len) == currStr.charAt(len)) {
                count = count + 1;
                let res = recursiveFn(str, favourites, pos + favourites[i].length, count)
                if (res.pos == str.length) {
                    counts.push(res.count)
                }
                count = count - 1
            }
        }
        return {
            pos: 0,
            count: 0
        }
    }

    return Math.min(...counts)

}

function backTrackingApproach1(str, favourites) {
    let map = {}
    favourites.forEach((s) => {
        map[s] = 1;
    })
    let a = check(0);
    return a

    function check(pos) {
        if (pos == str.length) {
            return 0;
        }
        let ans = Number.POSITIVE_INFINITY;
        let curr = "";
        for (let i = pos; i < str.length; i++) {
            curr += str[i];
            if (map[curr] == 1) {
                let other = check(i + 1);
                if (other != -1) {
                    ans = Math.min(ans, 1 + other)
                }
            }
        }
        return ans == Number.POSITIVE_INFINITY ? -1 : ans;
    }
}

function main() {
    let str = "iamasoftwaredeveloper"
    let favourites = ["am", "a", "m", "i", "softwa", "software", "red", "evelop", "er", "develope", "softwaredeveloper", "args", "slice", "redis", "enginner"];
    let res = backTrackingApproach(str, favourites);
    console.log(res);
    let res1 = backTrackingApproach1(str, favourites);
    console.log(res1);
}

main()
