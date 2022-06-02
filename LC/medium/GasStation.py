from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        fuel_remaining = 0
        least_starting_fuel = float("inf")
        start_city_index = -1

        for i in range(len(gas)):
            if fuel_remaining < least_starting_fuel:
                least_starting_fuel = fuel_remaining
                start_city_index = i
            fuel_remaining += gas[i] - cost[i]

        temp = start_city_index + 1
        fuel_remaining = 0
        for i in range(start_city_index, start_city_index + len(gas)):
            effective_index = i if i < len(gas) else i % len(gas)
            fuel_remaining += gas[effective_index] - cost[effective_index]

        return start_city_index if fuel_remaining >= 0 else -1

    def canCompleteCircuitv2(self, gas: List[int], cost: List[int]) -> int:
        fuel_remaining = 0
        least_starting_fuel = float("inf")
        start_city_index = -1

        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            if fuel_remaining < least_starting_fuel:
                least_starting_fuel = fuel_remaining
                start_city_index = i
            fuel_remaining += gas[i] - cost[i]
        return start_city_index


class GasStation:
    gas = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    x = Solution().canCompleteCircuitv2(gas, cost)
    print(x)
