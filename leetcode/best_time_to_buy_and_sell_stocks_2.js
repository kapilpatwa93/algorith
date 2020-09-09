// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
// 122. Best Time to Buy and Sell Stock II

var maxProfit = function(prices) {
    let count = 0;
    let l = prices.length-1
    for (let i=0;i<l;i++) {
        let diff = prices[i] - prices[i+1];
        count += diff < 0 ? diff : 0;
    }
    return count != 0 ? count *-1 : count;

};
function main() {
    let prices = [7,1,5,3,6,4];
    let res = maxProfit(prices);
    console.log(res);
}
main()





