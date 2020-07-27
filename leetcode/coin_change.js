// https://leetcode.com/problems/coin-change/
// 322. Coin Change
/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
let memo = {};
var coinChange = function (coins, amount) {
    memo = {};// reset the memo for new test case;
    return recurse(coins, amount, 0)
};

function getMem(num) {
    return memo[num] || Number.POSITIVE_INFINITY;
}

function recurse(coins, remaining, count) {
    if (remaining == 0) {
        return 0
    }
    if (remaining < 0) {
        return -1
    }
    if (memo[remaining]) {
        return getMem(remaining)
    }
    let minCount = Number.POSITIVE_INFINITY;
    for (let i = 0; i < coins.length; i++) {
        let res = recurse(coins, remaining - coins[i], count + 1)
        if (res != -1) {
            minCount = Math.min(minCount, res + 1)
        }
    }
    memo[remaining] = minCount != Number.POSITIVE_INFINITY ? minCount : -1;
    return minCount != Number.POSITIVE_INFINITY ? minCount : -1;
}

function main() {
    let coins = [1, 2, 5, 30]
    let amount = 33;
    let res = coinChange(coins, amount);
    console.log(res);
}

main()
