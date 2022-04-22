def validStartingCity(distances, fuel, mpg):
    fuel = list(map(lambda x: x * mpg, fuel))
    least_starting_fuel = 0
    leftover_fuel = 0
    result = 0
    for i in range(1, len(distances)):
        starting_fuel = leftover_fuel + fuel[i - 1] - distances[i - 1]
        leftover_fuel = starting_fuel
        if starting_fuel < least_starting_fuel:
            least_starting_fuel = starting_fuel
            result = i
    return result


class ValidStartingCity:
    distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10
    print(validStartingCity(distances, fuel, mpg))
