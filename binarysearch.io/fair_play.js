// https://binarysearch.io/problems/Fair-Pay
// Fair Pay
class Solution {
    solve(ratings) {
        let sum = new Array(ratings.length).fill(1);
        for (let i = 1; i < ratings.length; i++) {
            if (ratings[i - 1] < ratings[i]) {
                sum[i] = sum[i - 1] + 1
            }
        }
        for (let i = ratings.length - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1] && (sum[i] - sum[i + 1] < 1)) {
                sum[i] = sum[i + 1] + 1
            }
        }
        return sum.reduce((a, num) => num + a, 0)
    }
}

function main() {
    let ratings = [4, 3, 2, 1];
    let res = new Solution().solve(ratings);
    console.log(res);
}
main()
