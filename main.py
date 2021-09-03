import csv

#Prints out the full output of the csv file.
def open_csv_file(csv_file):
    data = []
    with open(csv_file, 'r', encoding='utf8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
        return data

fortnite_data = open_csv_file('Fortnite Data.csv')

#Returns the average number of kills of a specified number of players.
def average_kills(number_of_players):
    kills_total = 0
    count = 0
    for player in fortnite_data:
        if count < number_of_players:
            kills_total+=float(player[5])
            count+=1
    return kills_total / number_of_players

#Returns the average placement of a specified number of players.
def average_place(number_of_players):
    place_total = 0
    count = 0
    for player in fortnite_data:
        if count < number_of_players:
            place_total+=float(player[6])
            count+=1
    return place_total / number_of_players

#Returns the average points gained of a specified number of players.
def average_points(number_of_players):
    points_total = 0
    count = 0
    for player in fortnite_data:
        if count < number_of_players:
            points_total+=float(player[2])
            count+=1
    return points_total / number_of_players

#Returns the average games won of a specified number of players.
def average_wins(number_of_players):
    wins_total = 0
    count = 0
    for player in fortnite_data:
        if count < number_of_players:
            wins_total+=float(player[4])
            count+=1
    return wins_total / number_of_players

#Returns the average matches played of a specified number of players.
def average_matches(number_of_players):
    matches_total = 0
    count = 0
    for player in fortnite_data:
        if count < number_of_players:
            matches_total+=float(player[3])
            count+=1
    return matches_total / number_of_players