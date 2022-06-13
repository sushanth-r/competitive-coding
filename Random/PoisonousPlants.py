# https://www.hackerrank.com/challenges/poisonous-plants/problem

class Solution:
    def solve(self, plants) -> int:
        stack = []
        result = 0
        for i in range(len(plants) - 1, -1, -1):
            count = 0
            while stack and plants[i] < plants[stack[-1]]:
                stack.pop()
                count += 1
            stack.append(i)
            result = max(result, count)
        return result


class PoisonousPlants:
    plants = list(map(int, input().split()))
    x = Solution().solve(plants)
    print(x)
