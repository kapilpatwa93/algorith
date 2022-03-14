class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        final = []
        up = 0
        while len(paths) > 0:
            p = paths.pop()
            if p == "" or p == ".":
                continue
            if p == ".." and len(paths) > 0:
                up += 1
                # paths.pop()
            else:
                if up > 0:
                    up = up - 1
                else:
                    final.append(p)
        return "/" + "/".join(reversed(final))


if __name__ == '__main__':
    s = "/kapil//kapil/kapil/kapil/../../../kapil"
    res = Solution().simplifyPath(s)
    print(res)
