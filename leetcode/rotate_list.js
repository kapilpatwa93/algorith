// https://leetcode.com/problems/rotate-list/
// 61. Rotate List
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function (head, k) {
    let count = 0;
    let tail = head;
    while (tail) {
        count++;
        if (!tail.next) {
            break;
        }
        tail = tail.next;

    }
    if (!count) {
        return head
    }
    let pointer = head;
    tail.next = head;
    let splitByIndex = count - k % count;
    while (splitByIndex > 1) {
        pointer = pointer.next;
        splitByIndex--;
    }
    let newHead = pointer.next;
    pointer.next = null;
    return newHead;
};

function main() {
    let array = [1, 2, 3, 4, 5];
    let k = 8
    let head = getLinkedListFromArray(array);
    let res = rotateRight(head, k);
    let resArray = getArrayFromList(res);
    console.log(resArray);
}

main();

function getArrayFromList(head) {
    let pointer = head;
    let res = [];
    while (pointer) {
        res.push(pointer.val)
        pointer = pointer.next;
    }
    return res;
}

function getLinkedListFromArray(arr) {
    if (!arr.length) {
        return null
    }
    let head = new ListNode();
    let pointer = head;
    for (let i = 0; i < arr.length; i++) {
        pointer.val = arr[i];
        if (i === arr.length - 1) {
            pointer.next = null
        } else {
            pointer.next = new ListNode();
            pointer = pointer.next
        }

    }
    return head;
}

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}
