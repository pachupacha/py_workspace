import random
import time
import os

equipos = [
    "Real Madrid", "Barcelona", "Atletico Madrid", "Sevilla", "Real Sociedad", "Villarreal", "Athletic Club", "Valencia", "Real Betis", "Getafe",
    "Osasuna", "Celta de Vigo", "Espanyol", "Rayo Vallecano", "Mallorca", "Almeria", "Girona", "Cadiz", "Elche", "Granada"
]

historial_campeonatos = {equipo: 0 for equipo in equipos}
current_year = 2025

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def simulate_match(team1, team2, coef1, coef2):
    if random.random() < 0.0001:
        return "suspended", "racism"
    elif random.random() < 0.0005:
        return "suspended", "fireworks"
    elif random.random() < 0.001:
        return "suspended", "thrown objects"
    
    win_prob1 = coef1 / (coef1 + coef2)
    draw_prob = 0.25
    
    result = random.random()
    if result < win_prob1:
        return (random.randint(1, 4), random.randint(0, 2))
    elif result < win_prob1 + draw_prob:
        return (random.randint(0, 3), random.randint(0, 3))
    else:
        return (random.randint(0, 2), random.randint(1, 4))

def play_league(with_pauses):
    global current_year
    clear_screen()
    print(f"\n====================================")
    print(f"   WELCOME TO LALIGA {current_year}!")
    print(f"====================================")
    print("Experience the thrill of a full league season, where each match counts and unexpected events may occur.")
    print("Teams will battle for the title, and any previous champions will be displayed below.")
    
    if any(historial_campeonatos.values()):
        print("\nPrevious Champions:")
        for team, titles in historial_campeonatos.items():
            if titles > 0:
                print(f"- {team}: {titles} titles")
    
    print("\nLet the season begin! Simulating matches...")
    
    coefficients = {team: random.uniform(0.8, 1.2) for team in equipos}
    table = {team: {"points": 0, "goals_for": 0, "goals_against": 0, "goal_diff": 0} for team in equipos}
    
    matches = [(equipos[i], equipos[j]) for i in range(len(equipos)) for j in range(i + 1, len(equipos))]
    random.shuffle(matches)
    suspended_matches = []
    
    for i in range(0, len(matches), 10):
        matchday_matches = matches[i:i+10]
        for j, (team1, team2) in enumerate(matchday_matches):
            result = simulate_match(team1, team2, coefficients[team1], coefficients[team2])
            print(f"{team1} vs {team2}: {result}")
            
            if isinstance(result, tuple):
                goals1, goals2 = result
                if goals1 > goals2:
                    table[team1]["points"] += 3
                elif goals2 > goals1:
                    table[team2]["points"] += 3
                else:
                    table[team1]["points"] += 1
                    table[team2]["points"] += 1
                
                table[team1]["goals_for"] += goals1
                table[team2]["goals_for"] += goals2
                table[team1]["goals_against"] += goals2
                table[team2]["goals_against"] += goals1
                table[team1]["goal_diff"] = table[team1]["goals_for"] - table[team1]["goals_against"]
                table[team2]["goal_diff"] = table[team2]["goals_for"] - table[team2]["goals_against"]
            else:
                suspended_matches.append((team1, team2))
        
        if with_pauses:
            time.sleep(1.5)
            clear_screen()
    
    for team1, team2 in suspended_matches:
        result = simulate_match(team1, team2, coefficients[team1], coefficients[team2])
        goals1, goals2 = result
        
        if goals1 > goals2:
            table[team1]["points"] += 3
        elif goals2 > goals1:
            table[team2]["points"] += 3
        else:
            table[team1]["points"] += 1
            table[team2]["points"] += 1
    
    sorted_table = sorted(table.items(), key=lambda x: (-x[1]["points"], -x[1]["goal_diff"], -x[1]["goals_for"]))
    
    champion, stats = sorted_table[0]
    runner_up, runner_up_stats = sorted_table[1]
    if stats["points"] == runner_up_stats["points"] and stats["goal_diff"] == runner_up_stats["goal_diff"] and stats["goals_for"] == runner_up_stats["goals_for"]:
        result = simulate_match(champion, runner_up, coefficients[champion], coefficients[runner_up])
        goals1, goals2 = result
        champion = champion if goals1 > goals2 else runner_up
    
    historial_campeonatos[champion] += 1
    print(f"\n🏆 {champion} wins LaLiga {current_year}! Total titles: {historial_campeonatos[champion]}")
    current_year += 1

def main():
    while True:
        clear_screen()
        print(f"\n====================================")
        print(f"   WELCOME TO LALIGA {current_year}!")
        print(f"====================================")
        print("Experience the thrill of a full league season, where each match counts and unexpected events may occur.")
        print("Teams will battle for the title, and any previous champions will be displayed below.")
        print("\nWould you like to watch the simulation unfold with pauses or get instant results?")
        option = input("Enter 'y' for simulation with pauses or 'n' for instant results: ")
        play_league(with_pauses=option.lower() == "y")
        restart = input("Do you want to start a new season? (y/n): ")
        if restart.lower() != "y":
            break

if __name__ == "__main__":
    main()