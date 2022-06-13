class Solution:
    def appealSum(self, s: str) -> int:
        length = len(s)
        visited = {s[0]: 0}
        result = 1
        prev, curr = 1, 0
        for i in range(1, length):
            c = s[i]
            if c in visited:
                curr = prev + i - visited[c]
            else:
                curr = prev + i + 1
            visited[c] = i
            prev = curr
            result += curr
        return result


class TotalAppealOfAString:
    s = input()
    x = Solution().appealSum(s)
    print(x)
