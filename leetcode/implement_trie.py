class TrieNode:
    charMap = {}
    val = ""
    isWord = False

    def __init__(self, val, isWord):
        self.charMap = {}
        self.val = val
        self.isWord = isWord

    def insert(self, val, isWord):
        if val not in self.charMap:
            node = TrieNode(val, isWord)
            self.charMap[val] = node
        else:
            if isWord:
                self.charMap[val].isWord = True


class Trie:
    root = None

    def __init__(self):
        self.root = TrieNode("", False)

    def insert(self, word: str) -> None:
        currNode = self.root
        for i in range(len(word)):
            c = word[i]
            currNode.insert(c, i == len(word) - 1)
            currNode = currNode.charMap[c]

        return

    def search(self, word: str) -> bool:
        currNode = self.root
        isWord = False
        for c in word:
            if c not in currNode.charMap:
                return False
            isWord = currNode.charMap[c].isWord
            currNode = currNode.charMap[c]

        return isWord

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for c in prefix:
            if c not in currNode.charMap:
                return False
            currNode = currNode.charMap[c]
        return True


if __name__ == '__main__':
    obj = Trie()
    obj.insert("word")
    obj.insert("word1")
    obj.insert("word2")
    obj.insert("word3")
    obj.insert("word3")
    print(obj.search("word"))
    print(obj.startsWith("w"))
