// https://binarysearch.io/problems/Counting-Dinosaurs
// Counting Dinosaurs
class Solution {
    solve(animals, dinosaurs) {
        let animalMap = {};
        for (let i = 0; i < animals.length; i++) {
            animalMap[animals[i]] = ++animalMap[animals[i]] || 1;
        }
        let dSet = new Set(dinosaurs);
        let count = 0;
        for (let i of dSet.entries()) {
            count += animalMap[i[0]] || 0
        }
        return count;
    }
}

function main() {
    let animals = "ZZqBwgkqAIXoEmxGGJlvgQlEMktPgumTWsFzfXidNhkuFkhNMZwFQfcSHWZWYFflwfBowLLtEIngguwUnCilzUqAcdpdyfxWDzjbPFYSFPpBvxiZxSBZNYYkusCcWHC"
    let dinosaurs = "gmjYBiVKIBBziAxpwwMZmFlKuVTEOebxSHUIrRYRKtDmuwA"
    let res = new Solution().solve(animals,dinosaurs);
    console.log(res);
}

main();
