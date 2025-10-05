# CS111 - Electoral Votes Analysis Project 
This project analyse electoral votes in States within the US for a specific timeframe
# Overview
In the United States, the President is not elected by popular vote. Instead, they are chosen by the electoral college.

The electoral college consists of 538 electors from all 50 states and the District of Columbia (D.C.). Each state gets a number of electors based on its population (this number changes every decade after each census). D.C. is allocated 3 electors and treated as a state for purposes of the electoral college.

A majority of 270 electoral votes is required to elect the President. In 48 states and D.C., the winner of the state gets all the electoral votes for that state. Maine and Nebraska assign their electors using a proportional system.

Source: usa.gov

# Description
For this project, U.S. Presidential election results from 1976 to 2020 (inclusive) will be analyzed. Using datasets election_results.csv, which contains the election results for each state, and electoral_college.csv, which contains the number of electors of each state.

A program generated displays a menu with three options:
Get Election Results by State
Get Election Results by Electoral College
Get Election Results by Popular Vote

# *** Project: Analyzing U.S. Election Data ***
(Menu)
  Please choose one of the following options:
  1 - Get Election Results by State
  2 - Get Election Results by Electoral College
  3 - Get Election Results by Popular Vote
  0 - Quit

Enter option: 
- If option 1 is selected, the user will enter a year and a state and the program would display the election results for the given year and state (winner, number of votes, and percentage of total vote).
- If option 2 is selected, the user will enter a year and the program would display the election results for the given year by electoral college (winner, number of electoral votes, and percentage of electoral college).
- If option 3 is selected, the user will enter a year and the program would display the election results for the given year by popular vote (winner, number of votes, and percentage of total vote).
- After completing option 1, option 2, or option 3, the program returns to the main menu (as shown below) and start again. 
- If the user enters an integer that is not 0, 1, 2, or 3, the program outputs: "Invalid option. Please try again.", return to the main menu (as shown above), and start again.
This process is repeated until the user enters 0.

To get election results for a state and year, function get_election_results() is called from the driver helper module. This function receives a state and a year as input and returns a dictionary with the number of votes received by each candidate in the given state and year. If the state or year does not exist, it returns -1.

To get the number of electoral votes of a state in a year, function get_electoral_votes() is called from the driver helper module. This function receives a state and a year as input and returns the number of electoral votes of the given state in the given year. If the state or year does not exist, it returns -1.

Note: For simplicity, it is assumed that there are no ties and that every election is won by either the Democratic candidate or the Republican candidate (but you should still consider third-party candidates when determining the total number of votes). Additionally, all the electoral votes of a state (including Maine and Nebraska) is assigned to the winner of that state.

# Option 1 Demo:
<img width="1768" height="1512" alt="image" src="https://github.com/user-attachments/assets/0e5298dd-fd9a-4b2e-bfef-a18604223c8f" />

# Option 2 Demo:
<img width="1768" height="1512" alt="image" src="https://github.com/user-attachments/assets/d7ff00a8-64bb-459c-b805-d25767e7a2c3" />

# Option 3 Demo:
<img width="1768" height="1512" alt="image" src="https://github.com/user-attachments/assets/cd9851b3-5f4f-44bb-ba63-2ef671e7599e" />
