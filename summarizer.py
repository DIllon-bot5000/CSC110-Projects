###
### Author: Dillon Barr
### Course: CSC 110
### Description: This program reads a sporting event text file based on user requests and 
###              prints out a summary of the data that the file contains.

def open_file(teams, players, points):
    '''
    This function takes input from the user to open a file.
    It then splits the contents of the file in 3 lists used later on.
    The arguments passed to this function are empty lists declared in the main function.
    '''
    file_name = input('enter gamelog file name: \n')
    game_file = open(file_name, 'r')
    for line in game_file:
        line_split = line.split(' ')
        teams.append(line_split[0])
        players.append(line_split[1])
        points.append(int(line_split[2]))

def total_points(teams, points):
    '''
    This function tallys the points each team scored and stores them
    in respective variables.
    teams and points are lists being passed to this function.
    This function returns the variables holding the point totals.
    '''
    team1_points = 0
    team2_points = 0
    team1 = teams[0]
    for i in range(len(teams)):
        if teams[i] == team1:
            team1_points += points[i]
        else:
            team2 = teams[i]
            team2_points += points[i]
    return team1_points, team2_points, team1, team2

def remove_duplicates(players):
    '''
    This function takes the players list and removes the duplicate names
    to get an accurate count of players that scored.
    players is the list of all the player that scored.
    '''
    copied_list = players.copy()
    for i in copied_list:
        count = 0
        for j in copied_list:
            if i == j:
                count += 1
        while count > 1:
            copied_list.remove(i)
            count -= 1
    print(int(len(copied_list)), 'players scored.')


def game_summary(team1_points, team2_points, team1, team2, players):
    '''
    This function compares the point totals to determine the winner and prints
    out the some summary details of the game.
    team1_points and team2_points refer to the variable holding the teams point totals.
    team1 and team2 refer to the variable holding the name of the teams that played.
    players is a list of players being sent to the remove_duplicates function.
    '''
    if team1_points > team2_points:
        print(team1 + ' won!')
        print(team1 + ' scored', team1_points, 'points.')
        print(team2 + ' scored', team2_points, 'points.')

    else:
        print(team2 + ' won!')
        print(team1 + ' scored', team1_points, 'points.')
        print(team2 + ' scored', team2_points, 'points.')
    remove_duplicates(players)
    print(players[0] + ' scored first.')
    print(players[-1] + ' scored last.')

def main():
    teams = []
    players = []
    points = []
    team1_points = 0
    team2_points = 0
    open_file(teams, players, points)
    team1_points, team2_points, team1, team2 = total_points(teams, points)
    game_summary(team1_points, team2_points, team1, team2, players)
main()