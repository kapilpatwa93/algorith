package main

type MaxHeap struct {
	arr []int64
}

func (heap *MaxHeap) init(size int64) MaxHeap {
	return MaxHeap{arr: make([]int64,size)}
}

func (heap *MaxHeap) insert(data int64) (success bool, isFull bool) {
	success = false
	isFull = false
	if len(heap.arr) == cap(heap.arr) {
		isFull = true
	}
	heap.arr = append(heap.arr, data)
	for ; true; {

		break

	}
}
func (heap *MaxHeap) getDataFromIndex(index int) (int64, isValid) {
	if len(heap.arr) >= index {
		return heap.arr[index], true
	}
	return -1, false
}

func (heap *MaxHeap) delete() {

}

func (heap *MaxHeap) getLeftChildIndex(index int) (int, bool) {
	leftChildIndex := index * 2 + 1
	if len(heap.arr) >= leftChildIndex {
		return leftChildIndex, true
	}
	return -1, false
}

func (heap *MaxHeap) getRightChildIndex(index int) (int, bool) {

}

func (heap *MaxHeap) getParentIndex(index int) (int, bool) {

}

func (heap *MaxHeap) heapify() {

}

func main() {
	maxHeap := MaxHeap{}.init
}
