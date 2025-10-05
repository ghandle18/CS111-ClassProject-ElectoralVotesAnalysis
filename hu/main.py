import driver
STATE_NAMES = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
# Option 1 + 2: Function
def get_state_winner(state, year):
    if (year < 1976 or year > 2020):
        return -1
    elif year % 4 != 0:
        return -1
    elif state in STATE_NAMES:
        state_edata = driver.get_election_results(state,year)
        if state_edata['Democrat'] > state_edata['Republican']:
            winner = 'Democrat'
        else:
            winner = 'Republican'
        num_vote = state_edata[winner]
        per = (state_edata[winner]*100)/(state_edata['Democrat']+state_edata['Republican']+state_edata['Other'])
        #result = {"Winner": winner,'Votes': num_vote, 'Percentage': per}
        return winner, num_vote, per
    else: 
        return -1

# Option 2: Function
def get_electoral_college_winner(year):
    d_v = 0
    r_v = 0
    a_v = 0
    for state in STATE_NAMES:
        win = get_state_winner(state, year)
        a_v += driver.get_electoral_votes(state, year)
        if win[0] == 'Democrat':
            d_v += driver.get_electoral_votes(state, year)
        elif win[0] == 'Republican':
            r_v += driver.get_electoral_votes(state, year)
    if d_v>r_v:
        winner = 'Democrat'
        e_votes = d_v
        e_per = (d_v*100)/a_v
    else:
        winner = 'Republican'
        e_votes = r_v
        e_per = (r_v*100)/a_v
    return winner, e_votes, e_per 

# Option 3: Function
def get_popular_vote_winner(year):
    d_v = 0
    r_v = 0
    a_v = 0
    for state in STATE_NAMES:
        win = driver.get_election_results(state, year)
        d_v += win['Democrat']
        r_v += win['Republican']
        a_v += (win['Democrat']+win['Republican']+win['Other'])
    if d_v > r_v:
        winner = 'Democrat'
        votes = d_v
        percentage = (d_v*100)/a_v
    else:
        winner = 'Republican'
        votes = r_v
        percentage = (r_v*100)/a_v
    return winner, votes, percentage



if __name__ == '__main__': # Do not remove this line
    option = 1
    print("*** Project 02: Analyzing U.S. Election Data ***")
    # Case 0: Quit if option equals 0
    while option != 0:
        # Main Menu:
        print()
        print(f"Please choose one of the following options:")
        print(f"1 - Get Election Results by State")
        print(f"2 - Get Election Results by Electoral College")
        print(f"3 - Get Election Results by Popular Vote")
        print(f"0 - Quit")
        option = int(input("Enter option: "))
        # Case 1: Get election result by State
        if option == 1:
            year = int(input("Enter year: "))
            if (year < 1976 or year > 2020):
                print(f"Invalid year. Please try again.")
            elif year % 4 != 0:
                print(f"Invalid year. Please try again.")
            else:  
                state = input("Enter state name: ")
                if get_state_winner(state, year) == -1:
                    print(f"Invalid state name. Please try again.")
                else:
                    result = get_state_winner(state,year)
                    winner = result[0]
                    vote = result[1]
                    per = result[2]
                    print(f"Winner: {winner}")
                    print(f"Votes: {vote:,d}")
                    print(f"Percentage: {per:.2f}%")
        
        # Case 2: Get election result by Electoral College
        elif option == 2:
            year = int(input("Enter year: "))
            if (year < 1976 or year > 2020):
                print(f"Invalid year. Please try again.")
            elif year % 4 != 0:
                print(f"Invalid year. Please try again.")
            else:  
                result = get_electoral_college_winner(year)
                print(f"Winner: {result[0]}")
                print(f"Electoral Votes: {result[1]:,d}")
                print(f"Percentage: {result[2]:.2f}%")

        # Case 3: Get election results by Popular Vote
        elif option == 3:
            year = int(input("Enter year: "))
            if (year < 1976 or year > 2020):
                print(f"Invalid year. Please try again.")
            elif year % 4 != 0:
                print(f"Invalid year. Please try again.")
            else:  
                result = get_popular_vote_winner(year)
                print(f"Winner: {result[0]}")
                print(f"Votes: {result[1]:,d}")
                print(f"Percentage: {result[2]:.2f}%")

        # Case 4: Invalid option
        elif option != 0:
            print(f"Invalid option. Please try again.")
