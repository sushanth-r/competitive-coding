def tournamentWinner(competitions, results):
    teams = dict()
    max_score = 0
    winners = None
    for index in range(0, len(competitions)):
        home_team = competitions[index][0]
        away_team = competitions[index][1]
        result = results[index]
        previous_score = 0
        if result == 1:
            if home_team in teams:
                previous_score = teams[home_team]
            teams[home_team] = previous_score + 3
        else:
            if away_team in teams:
                previous_score = teams[away_team]
            teams[away_team] = previous_score + 3
    for team in teams:
        if max_score <= teams.get(team):
            max_score = teams.get(team)
            winners = team
    return winners


class TournamentWinner:
    competitions = [["A", "B"], ["B", "C"], ["C", "A"]]
    results = list(map(int, input().split()))
    print(tournamentWinner(competitions, results))
