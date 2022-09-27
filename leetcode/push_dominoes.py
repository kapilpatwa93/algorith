class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        p1 = 0
        p2 = 0
        if len(dominoes) <= 1:
            return dominoes
        res = list(dominoes)
        print(dominoes)
        #  in this fill the dominoes between "R....L"
        while p1 < len(dominoes) and p2 < len(dominoes):
            if dominoes[p1] == "R":
                p2 = p1 + 1
                process = True
                while p2 < len(dominoes):
                    if dominoes[p2] == "L":
                        break
                    if dominoes[p2] == "R":
                        process = False
                        p1 = p2
                        break
                    p2 += 1

                if p2 >= len(dominoes):
                    p1 = len(dominoes)
                    continue
                if not process:
                    continue
                a = p1
                b = p2
                while a <= b and a != b:
                    res[a] = "R"
                    res[b] = "L"
                    a += 1
                    b -= 1

                p1 = p2 + 1
            else:
                p1 += 1
        i = 1
        #  in this feel the dominoes which on Right side
        while i < len(res) - 1:
            if res[i - 1] == "R" and res[i] == "." and res[i + 1] != "L":
                res[i] = "R"
            i += 1

        if res[i - 1] == "R" and res[i] == ".":
            res[i] = "R"

        print("".join(res))
        i = len(res) - 2
        #  in this feel the dominoes which on Left side
        while i > 0:
            if res[i + 1] == "L" and res[i] == "." and res[i - 1] != "R":
                res[i] = "L"
            i -= 1
        if res[i + 1] == "L" and res[i] == ".":
            res[i] = "L"
        return "".join(res)


if __name__ == '__main__':
    dominoes = "R.R..L..L.R.R.L.."
    res = Solution().pushDominoes(dominoes)
    print(res)
