def Result(team1,team2):
    print('''TEAM 1 = Red Tshirt
Team 2 = Yellow Tshirt 
    ''')
    if team1==team2:
        return "Tie"
    elif team1>team2:
        return f"Team1 win by {team1-team2} runs"
    else:
        return f"Team2 win by {team2-team1} runs"
team1=int(input("Input Run of Team 1: "))
team2=int(input("Input Team2 run: "))
print(Result(team1,team2))