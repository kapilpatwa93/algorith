// https://leetcode.com/problems/bag-of-tokens/
// 948. Bag of Tokens
/**
 * @param {number[]} tokens
 * @param {number} P
 * @return {number}
 */
var bagOfTokensScore = function(tokens, P) {
    tokens.sort((a,b) => parseInt(a) - parseInt(b));
    let i = 0;
    let j = tokens.length -1;
    let points = 0;
    let maxPoints = points;
    while(i <= j) {
        let token = tokens[i]
        if(P >= token){
            P -= token;
            points++;
            i++
        } else if (P < token && points != 0) {
            P += tokens[j];
            points--;
            j--
        } else {
            break
        }
        maxPoints = Math.max(points,maxPoints);
    }
    return maxPoints

};
function main() {
    let tokens = [100,100,100,200,300,300,200,400];
    let p = 200;
    let res = bagOfTokensScore(tokens,p);
    console.log(res);
}
main()
