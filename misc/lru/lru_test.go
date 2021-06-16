package main

import "testing"

func BenchmarkLRURun(b *testing.B) {
	for i := 0; i < b.N; i++ {
		LRURun()
	}
}
func BenchmarkLRURun2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		LRURun2()
	}
}
