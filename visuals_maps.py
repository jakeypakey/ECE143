#This file holds the functions related to the chloropleth map visuals
#author: Srinivas Kakade
import processing
import numpy as np
import pandas as pd
from functools import reduce
from os import path
import json
import plotly.express as px
import plotly.graph_objects as go


#ALL FILE PATHS RELATIVE TO THOSE IN GIT REPO,
base = 'data/'

def Pres_Sen_data():
    '''This function processes data for Presedential and Senate races.
    '''
    PreSen=pd.read_csv('data\Pres_senate_2020_final.csv')
    PreSen['State_Abv']=PreSen['State']
    PreSen['Biden'],PreSen['Trump'], PreSen['Senate-D'],PreSen['Senate-R'] =PreSen['Biden']*100,PreSen['Trump']*100,PreSen['Senate-D']*100,PreSen['Senate-R']*100
    PreSen.set_index('State',inplace=True)
    PreSen['Pres_diff'] = PreSen['Biden']-PreSen['Trump'] #positive for Biden won
    PreSen['Sen_diff'] = PreSen['Senate-D']-PreSen['Senate-R'] #positive for Democratic candidate won
    PreSen['PreSen_diff_Biden'] = PreSen['Biden'] - PreSen['Senate-D'] #Positive for Good performance of Presidential candidate
    PreSen['PreSen_diff_Trump'] = PreSen['Trump'] - PreSen['Senate-R']

    for col in PreSen.columns:
        PreSen[col] = PreSen[col].astype(str)
    return PreSen

def presidential_race_visual():
    '''Returns a chloropleth map which shows whether Biden or Trump won in the given state. Darker color indicates that
        the candidate has won by larger margin.
    '''
    PreSen = Pres_Sen_data()
    PreSen['text'] ='Biden ='+ PreSen['Biden']+'<br>'+\
        'Trump ='+ PreSen['Trump']

    fig = go.Figure(data=go.Choropleth(
        locations= PreSen['State_Abv'], 
        z = PreSen['Pres_diff'], # Difference between vote share of Biden and Trump, positive values indicate Biden won.
        locationmode = 'USA-states', 
        colorscale = 'RdBu',
        zmin = -40,
        zmax = 40,
        text = PreSen['text'],
        colorbar_title = "Percentage Difference",
    ))

    fig.update_layout(
        title_text = 'Presidential Election',
        geo_scope='usa', # limite map scope to USA
    )
    fig.update_layout(title_font_size = 22)

    fig.show()
    return None

def senate_race_visual():
    ''' This function returns a chloropleth map that shows which party candidate won the senate race in the given state.
        Darker color indicates that the candidate has won by large margin.
    '''
    PreSen = Pres_Sen_data()
    PreSen['text1'] ='DEM ='+ PreSen['Senate-D']+'<br>'+\
        'REP ='+ PreSen['Senate-R']

    fig = go.Figure(data=go.Choropleth(
        locations= PreSen['State_Abv'], 
        z = PreSen['Sen_diff'], # difference between democratic and republic candidate vote share
        locationmode = 'USA-states',
        colorscale = 'RdBu',
        zmin = -40,
        zmax = 40,
        text = PreSen['text1'],
        colorbar_title = "Percentage Difference",
    ))

    fig.update_layout(
        title_text = 'Senate Election',
        geo_scope='usa', # limite map scope to USA
    )
    fig.update_layout(title_font_size = 22)

    fig.show()
    return None

def relative_performance_visual(cand):
    '''This function returns a chloropleth map showing relative performance of a presidential and senate candidate of
        the given party(cand = 'REP' or 'DEM'). Positive value indicates that the presidential candidate performed
        better than the senate candidate in that particular state.
    '''
    assert cand =='REP' or cand == 'DEM'
    if cand == 'REP':
        candidate, party, sen, diff  = 'Trump', 'Republican', 'Senate-D', 'PreSen_diff_Trump'
    else:
        candidate, party, sen, diff  = 'Biden', 'Democratic', 'Senate-R', 'PreSen_diff_Biden'
        
    PreSen = Pres_Sen_data()
    PreSen['text2'] ='Presidential Candidate ='+ PreSen[candidate]+'<br>'+\
        'Senate Candidate ='+ PreSen[sen]

    fig = go.Figure(data=go.Choropleth(
        locations= PreSen['State_Abv'], 
        z = PreSen[diff], # Difference between presidential and senate candidate vote share
        locationmode = 'USA-states',
        colorscale = 'BrBG',
        zmid = 0,
        text = PreSen['text2'],
        colorbar_title = "Percentage Difference",
    ))

    fig.update_layout(
        title_text = 'Relative Performance of '+ party +' Presidential and Senate Candidates',
        geo_scope='usa', # limite map scope to USA
    )
    fig.update_layout(title_font_size = 22)

    fig.show()
    return None

def pre_post_visual(cand,demo):
    '''This function returns a chloropleth maps that shows shift in pre/post election poll data for a given 
        candidate(cand = 'Biden' or 'Trump') among the given demographic group ('Male', 'Female', 'White', 'Black',
        'Hispanic/latino', 'White + BA/BS', 'White + No BA/BS', 'Republican', 'Democrat', 'Independent', '65+')
    '''
    assert isinstance(cand,str)
    assert isinstance(demo,str)
    Prepoll = processing.avgPolls(processing.readPreElectionPolls(),['Marist','Monmouth','Siena'])
    Postpoll = processing.readPostElectionPolls()
    dict_d={}
    post,pre = [], []
    # Extracting pre/post election poll data and the difference for particular demographic group.
    for i in Prepoll.index:
        if Prepoll.loc[i,'Candidate'] == cand:
            for j in Postpoll.index:
                if Postpoll.loc[j,'Candidate'] == cand and Prepoll.loc[i,'State'] == Postpoll.loc[j,'State']:     
                    dict_d[Prepoll.loc[i,'State']]=(Postpoll.loc[j,demo]-Prepoll.loc[i,demo])*100
                    pre.append(Prepoll.loc[i,demo]*100)
                    post.append(Postpoll.loc[j,demo]*100)
    Diff=pd.DataFrame.from_dict(dict_d,orient='index',dtype=None,columns=['diff'])
    Diff['pre']=pre
    Diff['post']=post
    #creating cloumn for state IDs for spatial coordinates
    Abbv=pd.read_csv('data\state_abbrev.csv')
    Abbv.set_index('State',inplace=True)
    Code,ind=[],[]
    for i in Diff.index:
        if i in Abbv.index:
            Code.append(Abbv.loc[i,'Code'])
            ind.append(i)
    Diff['State code']=Code   
    Diff['State']=ind
    
    #converting to strings so that the data can be displayed when hovered over particular state.
    for col in Diff.columns:
        Diff[col] = Diff[col].astype(str) 

    #text to be displayed when hovered over the map
    Diff['text'] = Diff['State']+ '<br>'+\
        'Prepolls ='+ Diff['pre']+'<br>'+\
        'Postpolls ='+ Diff['post']

    fig = go.Figure(data=go.Choropleth(
        locations= Diff['State code'], # Spatial coordinates
        z = Diff['diff'], # Difference between post and pre poll data
        locationmode = 'USA-states', # set of locations match entries in `locations`
        colorscale = 'Fall',
        reversescale=True,
        zmid = 0,
        text = Diff['text'],
        colorbar_title = ("Percentage Difference"),
        colorbar = dict(tickfont=dict(size=12)),
    
    )) 
    
    fig.update_layout(
        title_text ="Shift in pre/post-election poll data among "+ demo +" voters for " + cand,
        geo_scope='usa', # limite map scope to USA
    )
    fig.update_layout(title_font_size = 22)
   
    fig.show()
    return None
