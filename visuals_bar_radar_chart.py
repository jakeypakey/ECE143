#This file holds the functions related to the bar chart and radar chart visuals
#author: Fahim Talukder

import processing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Before creating the bar chart, we must process the input dataframes such that it will be feasible to plot
def barchart_processing(phone,mixed,online,demographic,state,candidate): 
    '''
    The purpose of this function is to take three existing DataFrames 
    and pull the polling data from those DataFrames to create a new
    DataFrame for a user-given demographic, state, and candidate
    
    :inPersonDF: a DataFrame that has the polling averages for all the phone polls
    :mixedDF: a DataFrame that has the polling data for the part online, part phone and text polls
    :onlineDF: a DataFrame that has the polling data for the completely online polls
    :demographic: this is the demographic that we want the side-by-side polling data for
    :candidate: this is the candidate that we want the above information for
    :state: this is the state for which we want the demographic data
    '''
    assert isinstance(phone,pd.DataFrame) #check that the input, phone, is a pandas dataframe
    assert isinstance(mixed,pd.DataFrame) #check that the input, mixed, is a pandas dataframe
    assert isinstance(online,pd.DataFrame) #check that the input, online, is a pandas dataframe
    assert isinstance(state,str) #check that the input, state, is a string
    assert isinstance(demographic,str) #check that the input, demographic, is a string
    assert isinstance(candidate,str) #check that the input, candidate, is a string

    #update phone to abstract the dataframe cell that has the demographic, state, and candidate of interest 
    phone = phone[(phone['State'] == state) & (phone['Candidate'] == candidate)][demographic] 
    #update mixed to abstract the dataframe cell that has the demographic, state, and candidate of interest 
    mixed = mixed[(mixed['State'] == state) & (mixed['Candidate'] == candidate)][demographic]
    #update online to abstract the dataframe cell that has the demographic, state, and candidate of interest 
    online = online[(online['State'] == state) & (online['Candidate'] == candidate)][demographic]
    #each of the above updated dataframes will hold only one value 

    phone = phone.to_dict() #convert each of the above dataframes to a dictionary
    mixed = mixed.to_dict()
    online = online.to_dict()
    
    phoneNew = {} #initialize three new dictionaries that will be filled in below
    mixedNew = {}
    onlineNew = {}
    #for each of the dictionaries that were converted from the dataframes (original), create a new key in the new dictionaries 
    #based on the methodology of the poll and set the corresponding value as the value from the original dictionary
    for key, value in phone.items(): 
        phoneNew["Phone"] = value #this dict has the phone polling value
    for key, value in mixed.items():
        mixedNew["Mixed"] = value #this dict has the mixed polling value
    for key, value in online.items():
        onlineNew["Online"] = value #this dict has the online polling value
    
    all3 = {**phoneNew,**mixedNew,**onlineNew} #merge all three dictionaries and save the result as a new dictionary
    finalDF = pd.DataFrame([all3]) #convert this dictionary that has the phone, mixed, and online values into a dataframe
    return finalDF

#This function is nearly the same as the above function, but it is for when we only want to display the phone and mixed polling results
def barchart_processing2(phone,mixed,demographic,state,candidate): 
    '''
    The purpose of this function is to take three existing DataFrames 
    and pull the polling data from those DataFrames to create a new
    DataFrame for a user-given demographic, state, and candidate
    
    :inPersonDF: a DataFrame that has the polling averages for all the phone polls
    :mixedDF: a DataFrame that has the polling data for the part online, part phone and text polls
    :demographic: this is the demographic that we want the side-by-side polling data for
    :candidate: this is the candidate that we want the above information for
    :state: this is the state for which we want the demographic data
    '''
    assert isinstance(phone,pd.DataFrame) #check that the input, phone, is a pandas dataframe
    assert isinstance(mixed,pd.DataFrame) #check that the input, mixed, is a pandas dataframe
    assert isinstance(state,str) #check that the input, state, is a string
    assert isinstance(demographic,str) #check that the input, demographic, is a string
    assert isinstance(candidate,str) #check that the input, candidate, is a string

    #update phone to abstract the dataframe cell that has the demographic, state, and candidate of interest 
    phone = phone[(phone['State'] == state) & (phone['Candidate'] == candidate)][demographic] 
    #update mixed to abstract the dataframe cell that has the demographic, state, and candidate of interest 
    mixed = mixed[(mixed['State'] == state) & (mixed['Candidate'] == candidate)][demographic]
    #update online to abstract the dataframe cell that has the demographic, state, and candidate of interest 

    phone = phone.to_dict() #convert each of the above dataframes to a dictionary
    mixed = mixed.to_dict()
    
    phoneNew = {} #initialize three new dictionaries that will be filled in below
    mixedNew = {}
    #for each of the dictionaries that were converted from the dataframes (original), create a new key in the new dictionaries 
    #based on the methodology of the poll and set the corresponding value as the value from the original dictionary
    for key, value in phone.items(): 
        phoneNew["Phone"] = value #this dict has the phone polling value
    for key, value in mixed.items():
        mixedNew["Mixed"] = value #this dict has the mixed polling value
    
    both = {**phoneNew,**mixedNew} #merge all three dictionaries and save the result as a new dictionary
    finalDF = pd.DataFrame([both]) #convert this dictionary that has the phone, mixed, and online values into a dataframe
    return finalDF

#Once the dataframes have been processed in a way that can be utilized for plotting the bar charts, this function will be called 
#to actually plot the bar charts
#the output to the bar chart processing function will be one of the inputs to the plot bar chart function
#either of the two above functions' outputs can be used as an input here
def plot_bar_chart(df,demographic,state,candidate):
    '''
    The objective of this function is to take the output of the bar chart processing script, which is a DataFrame, 
    and utilize it as an input to this function so that a bar chart can be plotted
    
    :df: input dataframe whose columns reflect the different methodologies (phone, mixed, and online) 
    used in calculation of pre-election polling data  
    :demographic: demographic that the data is for 
    :state: state in which the demographic is located
    :candidate: candidate support amongst the demographic specified
    
    Unfortunately, the DataFrame input does not include the demographic, state, and candidate for which the data is for,
    so those have to be inputted once more for the axis and title
    '''
    assert isinstance(df,pd.DataFrame) #check that the input, df, is a dataframe
    assert isinstance(demographic,str) #check that the input, demographic, is a string
    assert isinstance(state,str) #check that the input, state, is a string
    assert isinstance(candidate,str) #check that the input, candidate, is a string
    
    ax = df.plot.bar(figsize=(7,6),rot=0) #create the bar plot based on the dataframe
    ax.set_xlabel(demographic,fontsize=19) #label the x-axis
    ax.set_ylabel("Percentage of Support",fontsize=19) #label the y-axis
    ax.set_title("Support Among " + demographic + " for " + candidate + " in " + state, fontsize=17, pad=15) #the title
    #ex: Support Among Independents for Trump in Iowa
    ax.legend(fontsize=11) #the legend, the legend keys are automatic based on the column names from the df
    ax.xaxis.labelpad = 15 #padding of x-axis
    ax.yaxis.labelpad = 15 #padding of y-axis
    ax.tick_params(labelsize=15) #make the y-axis ticks easier to read
    ax.tick_params( #hide the x-axis ticks
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=False,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        labelbottom=False) # labels along the bottom edge are of


#The following function is for creating and plotting the radar charts
def radar_plot(df, state, candidate, demographics, clr):
    '''
    The objective of this function is to take a select row from the inputted dataframe and output the demographic (columns) data
    for that row in the form of a radar chart
    
    :df: input dataframe in which we will use the inputted state and candidate to narrow down to single row
         dataframe can be any output from readPreElectionPolls(), readPostElectionPolls
    :state: state for which we want demographic info from, string
    :candidate: candidate for which we want demographic info for, string
    :demographics: this is a list of demographics that the user wants within the radar plot, list
    :color: the color that the user wants the plot to be outlined and filled in as
    '''
    assert isinstance(df,pd.DataFrame) #check that the input, df, is a pandas dataframe
    assert isinstance(state,str) #check that the input, state, is a string
    assert isinstance(candidate,str) #check that the input, candidate, is a string
    assert isinstance(demographics,list) #check that the input, demographics, is a string
    assert isinstance(clr,str) #check that the input, clr, is a string #clr represents color
    df = df[(df['State'] == state) & (df['Candidate'] == candidate)] #obtain the row that has the specified state and candidate
    df = df.set_index('State') #instead of indexing by the ID, we want to index by the state(s) to retrieve the data below
    df = df.drop(columns=[col for col in df if col not in demographics]) #drop the columns that do not pertain to the demographics we desire to display
    values = df.loc[state].tolist() #returns a list of the values from the respective demographics
    num_dems = len(demographics) #get the number of demographics from the list
    angles = np.linspace(0, 2 * np.pi, num_dems, endpoint=False).tolist() #Split the circle into even parts and save the angles so we know where to put each axis
    values += values[:1] #The plot is a circle, so we need to "complete the loop"
    angles += angles[:1] #by appending the start value to the end
    fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True)) # ax = plt.subplot(polar=True)
    ax.plot(angles, values, color=clr, linewidth=1) # Draw the outline of our data
    ax.fill(angles, values, color=clr, alpha=0.25)  # Fill it in
    ax.set_theta_offset(np.pi / 2) #Fix axis to go in the right order and start at 12 o'clock
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles), demographics,fontsize=20) #Draw axis lines for each angle and demographic
    #Go through labels and adjust alignment based on where it is in the circle
    for label, angle in zip(ax.get_xticklabels(), angles):
        if angle in (0, np.pi):
            label.set_horizontalalignment('center')
        elif 0 < angle < np.pi:
            label.set_horizontalalignment('left')
        else:
            label.set_horizontalalignment('right')
    ax.set_rgrids([0.1, 0.2, 0.3, 0.4, 0.5,0.6,0.7]) #setting gridlines manually
    #ax.set_rgrids([0.1, 0.2, 0.3, 0.4, 0.5])
    ax.set_rlabel_position(180 / num_dems) #Set position of y-labels to be in the middle of the first two axes
    ax.tick_params(colors='#222222') # Change the color of the tick labels.
    ax.tick_params(axis='y', labelsize=12) # Make the y-axis labels smaller.
    ax.grid(color='#AAAAAA') # Change the color of the circular gridlines.
    ax.spines['polar'].set_color('#222222')  # Change the color of the outermost gridline (the spine)
    ax.set_facecolor('#FAFAFA') # Change the background color inside the circle itself.
    ax.set_title(candidate + ' in ' + state, y=1.08, fontsize=24) #give the chart a title #ex: Trump in Arizona