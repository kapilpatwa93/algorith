// https://leetcode.com/problems/top-k-frequent-words/solution/
// 692. Top K Frequent Words
package main

import (
	"fmt"
	"sort"
)

type Count struct {
	word string
	freq int
}

func topKFrequent(words []string, k int) []string {
	freqMap := make(map[string]int)
	topKWords := make([]string, 0)
	for _, word := range words {
		freqMap[word] += +1
	}
	wordCount := make([]Count, 0)
	for key, val := range freqMap {
		wordCount = append(wordCount, Count{
			word: key,
			freq: val,
		})
	}
	sort.Slice(wordCount, func(i, j int) bool {
		return wordCount[i].freq > wordCount[j].freq || (wordCount[i].freq == wordCount[j].freq && wordCount[i].word < wordCount[j].word)
	})
	for i := 0; i < k; i++ {
		topKWords = append(topKWords, wordCount[i].word)
	}
	return topKWords
}

func main() {
	a := []string{"sa", "ka", "ssaa", "dsa", "dsa", "ka", "a", "b", "b"}
	k := 2
	res := topKFrequent(a, k)
	fmt.Println(res)
}
