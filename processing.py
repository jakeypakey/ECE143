#Processing file with utility functions better
#left out of the notebook to reduce clutter
import numpy as np
import pandas as pd
###############
#ALL FILE PATHS RELATIVE TO THOSE IN GIT REPO,
#change this to change base data dir
base = 'data/'
###############


def statesTotals(showThirdParty=False):
    df = pd.read_csv(base+'kaggle_data/president_county_candidate.csv')

    #each state will have a dictionary of candidates, where the keys are vote totals
    states = {k:dict() for k in df['state'].unique()}

    #first determine ALL candidates, then fetch parties (there is overlap sometimes)
    candidates = dict()
    for can in df['candidate'].unique():
        #assign candidate `can` their party affiliation
        candidates[can] = df[df['candidate'] == can].iloc[0]['party']

    #setup states dictionary
    for state in states.keys():
        for can in df[df['state'] == state]['candidate'].unique():
            #initialize every states vote total to 0 for each cadidate,party pair
            states[state][(can,candidates[can])] = 0

    #match column names with kaggle data for consistency
    #now tally up votes for each candidate by state
    for state in states.keys():
        for can,par in states[state].keys():
            states[state][(can,par)] = (df[ (df['state']==state) & (df['candidate']==can) & (df['party']==par)]['total_votes'].sum())
   
    #unpack and convert dictionary
    ret = dict()
    ret = {k:[] for k in ['state','candidate','party','total_votes']}
    for state in states.keys():
        thirdCount = 0
        for key in states[state].keys():
            if not showThirdParty and not(key[1]=="REP" or key[1]=="DEM"):
                thirdCount+=states[state][key]
            else:
                ret['state'].append(state)
                ret['candidate'].append(key[0])
                ret['party'].append(key[1])
                ret['total_votes'].append(states[state][key])
        #at the of each state, fill in third party if needed
        if not showThirdParty:
            ret['state'].append(state)
            ret['candidate'].append("Other")
            ret['party'].append("N/A")
            ret['total_votes'].append(thirdCount)

    return pd.DataFrame(ret)

def readPolls(showMinorityByGroup=True):
    pollsters = ['Emerson','Marist','Monmouth','Siena']
    candidates = ['Biden','Trump']
    dfs = []
    for poll in pollsters:
        for can in candidates:
            dfs.append(pd.read_csv(base+'pre_election_polls/'+poll+'_'+can.lower()+'.csv'))
            dfs[-1]['Candidate'] = can
            dfs[-1]['Pollter'] = poll
    for df in dfs:
        print(df.head())



readPolls()
