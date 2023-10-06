# Tournement Winner
# There's an algorithms tournament taking place in which teams of programmers
# Two teams compete against each other and receive a point for each,
# problem they solve correctly. The tournament is formatted as a round robin,
#
# where each team faces off against all other teams. Only two teams compete
# against each other at a time, and for each competition, one team is designated
#
# When you win a competition, you receive 3 points; when you lose, you receive 0
# It's guaranteed that there will be no ties in the tournament.
#
# First Argument: Competitions
# * Array of pairs representing all of the competitions in the tournament.
# * Pairs are in the form of [home_team, away_team], where each team is a string of at most 30 characters representing the name of the team.
#
# Second Argument: Results
# * Array of integers representing the winner of each corresponding competition in the competitions array.
# * results[i] denotes the winner of competitions[i],
#   where
#       a 1 in the results array means that the home team in the corresponding competition won and
#       a 0 means that the away team won.
#
#
competition = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"],
]

results = [0,0,1]

# Solution 1: O(n) time | O(k) space
# Where n is the number of competitions and k is the number of teams
def tournoment_winner(competitors, results):
    best_team = ""
    scores = {}

    for index, competition in enumerate(competitors):
        result = results[index]
        home_team, away_team = competition

        winning_team = home_team if result == 1 else away_team

        update_scores(winning_team, 3, scores)

        if scores[winning_team] > scores[best_team]:
            best_team = winning_team

    return best_team

def update_scores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points
