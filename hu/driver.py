"""
    driver.py
    Project 2: Analyzing U.S. Election Data
    Copyright © 2024 Gonzalo Bello. All rights reserved.
"""

import pandas as pd # import library
election_results = pd.read_csv("election_results.csv") # load dataset
electoral_college = pd.read_csv("electoral_college.csv") # load dataset

def get_electoral_votes(state, year):
    """Returns number of electoral votes for given state and year"""
    year = str(year)
    result = electoral_college.loc[electoral_college["state"] == state, year]
    if result.shape[0] == 0: # if given state is not in dataset
        return -1
    else:
        return int(result.to_string(index = False)) # returns number of electoral votes

def get_election_results(state, year):
    """Returns election results for given state and year"""
    state = state.upper()
    data = election_results[(election_results["year"] == year) & (election_results["state"] == state)]
    if data.shape[0] == 0: # if given state or year is not in dataset
        return -1
    else:
        dem_candidate = get_candidate(state, year, "DEMOCRAT")
        rep_candidate = get_candidate(state, year, "REPUBLICAN")
        votes_dem = data.loc[data["candidate"] == dem_candidate, "candidatevotes"].sum()
        votes_rep = data.loc[data["candidate"] == rep_candidate, "candidatevotes"].sum()
        votes_other = data.loc[(data["candidate"] != dem_candidate) & (data["candidate"] != rep_candidate), "candidatevotes"].sum()
        result = {
            "Democrat": votes_dem,
            "Republican": votes_rep,
            "Other": votes_other
        }
        return result # returns election results

def get_candidate(state, year, party):
    """Returns candidate for given state, year, and party"""
    candidate = election_results.loc[(election_results["year"] == year) & (election_results["state"] == state) & (election_results["party_simplified"] == party), "candidate"]
    return candidate.iloc[0] # returns candidate