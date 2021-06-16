package main

import (
	"container/list"
)

type CustomList struct {
	head *Node
	tail *Node
}
type Node struct {
	next *Node
	prev *Node
	data interface{}
}

func NewList() CustomList {
	return CustomList{
		tail: nil,
		head: nil,
	}
}

func (l *CustomList) Delete(n *Node) {
	if n == l.head {
		l.head = n.next
	}
	if n == l.tail {
		l.tail = n.prev
	}
	if n.prev != nil {
		n.prev.next = n.next
	}
	if n.next != nil {
		n.next.prev = n.prev
	}
}

func (l *CustomList) Insert(key, data int) *Node {
	node := Node{
		next: nil,
		prev: nil,
		data: Data{
			key: key,
			val: data,
		},
	}
	if l.head == nil {
		l.head = &node
	} else {
		node.next = l.head
		l.head.prev = &node
		l.head = &node
	}
	if l.tail == nil {
		l.tail = &node
	}
	return &node
}

type LRUCache struct {
	capacity int
	pageMap  map[int]*Node
	list     CustomList
}

type LRUCache2 struct {
	capacity int
	pageMap  map[int]*list.Element
	list     *list.List
}
type Data struct {
	key int
	val int
}

func Constructor(capacity int) LRUCache {
	return LRUCache{
		capacity: capacity,
		pageMap:  make(map[int]*Node),
		list:     NewList(),
	}
}

func Constructor2(capacity int) LRUCache2 {
	return LRUCache2{
		capacity: capacity,
		pageMap:  make(map[int]*list.Element),
		list:     list.New(),
	}
}

func (this *LRUCache2) Get(key int) int {
	if node, exist := this.pageMap[key]; exist {
		this.list.MoveToFront(node)
		return node.Value.(Data).val
	}
	return -1
}
func (this *LRUCache2) Put(key, value int) {
	if node, exist := this.pageMap[key]; exist {
		this.list.Remove(node)

	} else {
		if len(this.pageMap) >= this.capacity {
			node := this.list.Remove(this.list.Back()).(Data)
			delete(this.pageMap, node.key)
		}
	}
	node := Data{
		key: key,
		val: value,
	}
	this.pageMap[key] = this.list.PushFront(node)

}

func (this *LRUCache) Get(key int) int {
	value, exist := this.pageMap[key]
	if exist {
		this.list.Delete(value)
		data := value.data.(Data)
		this.pageMap[key] = this.list.Insert(data.key, data.val)
		return data.val
	}
	return -1
}

func (this *LRUCache) Put(key int, value int) {
	_, exist := this.pageMap[key]
	if exist {
		this.list.Delete(this.pageMap[key])
		delete(this.pageMap, key)
	} else if len(this.pageMap) >= this.capacity {
		tail := this.list.tail
		this.list.Delete(tail)
		delete(this.pageMap, tail.data.(Data).val)
	}
	this.pageMap[key] = this.list.Insert(key, value)
	return
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
func LRURun() {
	var lruCache LRUCache

	commands := []string{"LRUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put", "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get", "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put", "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put", "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put", "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"}
	values := [][]int{{10}, {10, 13}, {3, 17}, {6, 11}, {10, 5}, {9, 10}, {13}, {2, 19}, {2}, {3}, {5, 25}, {8}, {9, 22}, {5, 5}, {1, 30}, {11}, {9, 12}, {7}, {5}, {8}, {9}, {4, 30}, {9, 3}, {9}, {10}, {10}, {6, 14}, {3, 1}, {3}, {10, 11}, {8}, {2, 14}, {1}, {5}, {4}, {11, 4}, {12, 24}, {5, 18}, {13}, {7, 23}, {8}, {12}, {3, 27}, {2, 12}, {5}, {2, 9}, {13, 4}, {8, 18}, {1, 7}, {6}, {9, 29}, {8, 21}, {5}, {6, 30}, {1, 12}, {10}, {4, 15}, {7, 22}, {11, 26}, {8, 17}, {9, 29}, {5}, {3, 4}, {11, 30}, {12}, {4, 29}, {3}, {9}, {6}, {3, 4}, {1}, {10}, {3, 29}, {10, 28}, {1, 20}, {11, 13}, {3}, {3, 12}, {3, 8}, {10, 9}, {3, 26}, {8}, {7}, {5}, {13, 17}, {2, 27}, {11, 15}, {12}, {9, 19}, {2, 15}, {3, 16}, {1}, {12, 17}, {9, 1}, {6, 19}, {4}, {5}, {5}, {8, 1}, {11, 7}, {5, 2}, {9, 28}, {1}, {2, 2}, {7, 4}, {4, 22}, {7, 24}, {9, 26}, {13, 28}, {11, 26}}
	res := make([]int, 0)
	for i := 0; i < len(commands); i++ {
		switch commands[i] {
		case "LRUCache":
			lruCache = Constructor(values[i][0])
			res = append(res, -1111)
		case "get":
			val := lruCache.Get(values[i][0])
			res = append(res, val)
		case "put":
			lruCache.Put(values[i][0], values[i][1])
			_ = append(res, -1111)
		}
	}
}
func LRURun2() {
	var lruCache2 LRUCache2

	commands := []string{"LRUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put", "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get", "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put", "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put", "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put", "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"}
	values := [][]int{{10}, {10, 13}, {3, 17}, {6, 11}, {10, 5}, {9, 10}, {13}, {2, 19}, {2}, {3}, {5, 25}, {8}, {9, 22}, {5, 5}, {1, 30}, {11}, {9, 12}, {7}, {5}, {8}, {9}, {4, 30}, {9, 3}, {9}, {10}, {10}, {6, 14}, {3, 1}, {3}, {10, 11}, {8}, {2, 14}, {1}, {5}, {4}, {11, 4}, {12, 24}, {5, 18}, {13}, {7, 23}, {8}, {12}, {3, 27}, {2, 12}, {5}, {2, 9}, {13, 4}, {8, 18}, {1, 7}, {6}, {9, 29}, {8, 21}, {5}, {6, 30}, {1, 12}, {10}, {4, 15}, {7, 22}, {11, 26}, {8, 17}, {9, 29}, {5}, {3, 4}, {11, 30}, {12}, {4, 29}, {3}, {9}, {6}, {3, 4}, {1}, {10}, {3, 29}, {10, 28}, {1, 20}, {11, 13}, {3}, {3, 12}, {3, 8}, {10, 9}, {3, 26}, {8}, {7}, {5}, {13, 17}, {2, 27}, {11, 15}, {12}, {9, 19}, {2, 15}, {3, 16}, {1}, {12, 17}, {9, 1}, {6, 19}, {4}, {5}, {5}, {8, 1}, {11, 7}, {5, 2}, {9, 28}, {1}, {2, 2}, {7, 4}, {4, 22}, {7, 24}, {9, 26}, {13, 28}, {11, 26}}
	//commands := []string{"LRUCache","put","put","put","put","put","get", "get","get", "put", "put", "get", "get"}
	//values := [][]int{{3},{1,11},{2,22},{3,33},{4,44}, {3,333},{2},{3}, {2}, {4,444}, {4,4444}, {3}, {3}}

	res2 := make([]int, 0)
	for i := 0; i < len(commands); i++ {
		switch commands[i] {
		case "LRUCache":
			lruCache2 = Constructor2(values[i][0])
			res2 = append(res2, -1111)
		case "get":
			val2 := lruCache2.Get(values[i][0])
			res2 = append(res2, val2)
		case "put":
			lruCache2.Put(values[i][0], values[i][1])
			_ = append(res2, -1111)
		}
	}
}
func main() {
	LRURun()
	LRURun2()

}

//[null,null,null,null,null,4,3,2,-1,null,-1,2,3,-1,5]
//ull, null, 1, null, -1, null, -1, 3, 4]

//[null,null,null,null,null,null,-1,null,19,17,null,-1,null,null,null,-1,  null,-1, 5,-1, 12, null,null,3, 5,5,null,null,1, null,-1,null, 30,5,30, null,null,null,-1 ,null,-1 ,24, null,null,18, null,null,null,null,14,null,null,18,null,null,-1,null,null,null,null,null,18,null,null,24,null,4,29,30,null,12,-1,null,null,null,null,-1,null,null,null,null,17,22,-1,null,null,null,24,null,null,null,20,null,null,null,29,-1,-1,null,null,null,null,20,null,null,null,null,null,null,null]
//[null,null,null,null,null,null,-1,null,19,17,null,-1,null,null,null,-1,  null,-1, 5,-1, 12, null,null,3, 5,5,null,null,1, null,-1,null, 30,5,30, null,null,null,-1, null,-1 ,24, null,null,18, null,null,null,null,-1,null,null,18,null,null,-1,null,null,null,null,null,18,null,null,-1,null,4,29,30,null,12,-1,null,null,null,null,29,null,null,null,null,17,22,18,null,null,null,-1,null,null,null,20,null,null,null,-1,18,18,null,null,null,null,20,null,null,null,null,null,null,null]

//todo debug dd[0] == 10 and dd[1] == 13
