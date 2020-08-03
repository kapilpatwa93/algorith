function MinHeap() {
    this._arr = [];
}

MinHeap.prototype.valueOf = function () {
    return this._arr.join(" ");
}

MinHeap.prototype.decreaseKey = function (i) {
    console.log(this._arr);
    heapify.call(this);
}

MinHeap.prototype.delete = function () {
    let data = getDataByIndex.call(this, 0);
    if (data) {
        setDataAtIndex.call(this, 0, popData.call(this));
        heapify.call(this, 0);

    }
    return data
}

MinHeap.prototype.insert = function (data) {
    let currentIndex = pushData.call(this, data);
    let parentIndex = getParentIndex(currentIndex);
    let getData = getDataByIndex.bind(this);
    let swapNodes = swapNodesByIndex.bind(this);
    while (parentIndex !== -1) {
        if (getData(currentIndex) < getData(parentIndex)) {
            swapNodes(currentIndex, parentIndex);
        }
        currentIndex = parentIndex
        parentIndex = getParentIndex(parentIndex);
    }
}

function popData() {
    return this._arr.pop() || null;
}

function pushData(data) {
    this._arr.push(data);
    return this._arr.length - 1;

}

function swapNodesByIndex(i, j) {
    let temp = getDataByIndex.call(this, i);
    setDataAtIndex.call(this, i, getDataByIndex.call(this, j));
    setDataAtIndex.call(this, j, temp);

}

function getDataByIndex(index) {
    return index >= 0 && index < this._arr.length ? this._arr[index] : null;
}

function setDataAtIndex(index, data) {
    if (index >= 0 && index < this._arr.length) {
        this._arr[index] = data;
        return true;
    }
    return false;
}

// returns -1 for invalid Index
function getParentIndex(childIndex) {
    return Math.ceil(childIndex / 2) - 1;
}

function getLeftChildIndex(parentIndex) {
    return parentIndex * 2 + 1
}

function getRightChildIndex(parentIndex) {
    return (parentIndex + 1) * 2
}

function heapify(subtreeRootIndex) {
    let getData = getDataByIndex.bind(this);
    let leftChildIndex = getLeftChildIndex(subtreeRootIndex)
    let leftChild = getData(leftChildIndex);
    let rightChildIndex = getRightChildIndex(subtreeRootIndex)
    let rightChild = getData(rightChildIndex);
    let root = getData(subtreeRootIndex);
    let swapBy;
    if (leftChild && leftChild < root) {
        swapBy = leftChildIndex;
        if (rightChild && rightChild < leftChild ) {
            swapBy = rightChildIndex
        }
    } else if (rightChild && rightChild < root) {
        swapBy = rightChildIndex;
        if (leftChild &&  leftChild < rightChild) {
            swapBy = leftChildIndex
        }

    }
    if (swapBy) {
        swapNodesByIndex.call(this,subtreeRootIndex,swapBy);
        heapify.call(this,swapBy)
    }
}
module.exports = MinHeap;
