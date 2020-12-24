package main

import "fmt"

type List struct {
	head *Node
	tail *Node
}
type Node struct {
	next *Node
	prev *Node
	data int
	key  int
}

func NewList() List {
	return List{
		tail: nil,
		head: nil,
	}
}

func (l *List) Delete(n *Node) {
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
func (l *List) Insert(key, data int) *Node {
	node := Node{
		next: nil,
		prev: nil,
		data: data,
		key:  key,
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
	list     List
}

func Constructor(capacity int) LRUCache {
	return LRUCache{
		capacity: capacity,
		pageMap:  make(map[int]*Node),
		list:     NewList(),
	}
}

func (this *LRUCache) Get(key int) int {
	value, exist := this.pageMap[key]
	if exist {
		node := this.pageMap[key]
		this.list.Delete(node)
		node = this.list.Insert(node.key, node.data)
		this.pageMap[key] = node
		return value.data
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
		delete(this.pageMap, tail.key)
	}
	this.pageMap[key] = this.list.Insert(key, value)
	return
}

func LRURun() {
	var lruCache LRUCache
	commands := []string{"LRUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put", "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get", "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put", "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put", "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put", "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"}
	values := [][]int{{10}, {10, 13}, {3, 17}, {6, 11}, {10, 5}, {9, 10}, {13}, {2, 19}, {2}, {3}, {5, 25}, {8}, {9, 22}, {5, 5}, {1, 30}, {11}, {9, 12}, {7}, {5}, {8}, {9}, {4, 30}, {9, 3}, {9}, {10}, {10}, {6, 14}, {3, 1}, {3}, {10, 11}, {8}, {2, 14}, {1}, {5}, {4}, {11, 4}, {12, 24}, {5, 18}, {13}, {7, 23}, {8}, {12}, {3, 27}, {2, 12}, {5}, {2, 9}, {13, 4}, {8, 18}, {1, 7}, {6}, {9, 29}, {8, 21}, {5}, {6, 30}, {1, 12}, {10}, {4, 15}, {7, 22}, {11, 26}, {8, 17}, {9, 29}, {5}, {3, 4}, {11, 30}, {12}, {4, 29}, {3}, {9}, {6}, {3, 4}, {1}, {10}, {3, 29}, {10, 28}, {1, 20}, {11, 13}, {3}, {3, 12}, {3, 8}, {10, 9}, {3, 26}, {8}, {7}, {5}, {13, 17}, {2, 27}, {11, 15}, {12}, {9, 19}, {2, 15}, {3, 16}, {1}, {12, 17}, {9, 1}, {6, 19}, {4}, {5}, {5}, {8, 1}, {11, 7}, {5, 2}, {9, 28}, {1}, {2, 2}, {7, 4}, {4, 22}, {7, 24}, {9, 26}, {13, 28}, {11, 26}}
	res := make([]int, 0)
	for i := 0; i < len(commands); i++ {
		switch commands[i] {
		case "LRUCache":
			lruCache = Constructor(values[i][0])
			res = append(res, -11)
		case "get":
			val := lruCache.Get(values[i][0])
			res = append(res, val)
		case "put":
			lruCache.Put(values[i][0], values[i][1])
			_ = append(res, -11)
		}
	}
	fmt.Println(res)
}
func main() {
	LRURun()

}
