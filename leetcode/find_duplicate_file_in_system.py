from typing import List
import re


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        fileMap = {}
        for path in paths:
            splits = path.split(" ")
            directory = splits[0]
            for files in splits[1:]:
                content = re.findall(r'\(.*?\)', files)[0][1:-1]
                filePath = [directory + "/" + files.split("(")[0]]
                fileMap[content] = fileMap[content] + filePath if content in fileMap else filePath

        arr = filter(lambda x: len(x) > 1, fileMap.values())
        return list(arr)


if __name__ == '__main__':
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
    res = Solution().findDuplicate(paths)
    print(res)
