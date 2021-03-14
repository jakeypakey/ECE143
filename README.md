# ECE143 Final Project Team 8
Debugging the 2020 Election Predictions

This repository holds the project for ECE 143 during Winter 2021 at the University of California, San Diego.
It contains all the files and code utilized within this project.

# Group Members
Gregory Fields, Fahim Talukder, Jacob Pollard, Srinivas Kakade, Zhehui Li

# Problem
There were glaring disparities between polling predictions and the actual election outcomes for the 2020 election
as polling underestimated the proportion of votes Donald Trump ended up receiving. The aforementioned
disparities varied by region and were particularly pronounced in the upper midwest, but Trump also outperformed
expectations among certain demographic groups. 

# Objective
Our intention is to compare and analyze the shift between exit polls for the 2020 general election and a variety of
pre-election polls. This analysis will focus on finding correlations between these shifts and the various regions and 
demographics specified in the exit polling data. In order to do the aforementioned, we had to process the data we used
into dataframes that were organized by state, candidate, pollster, and the various demographics (male, female, White, Black,
Hispanic/Latino, Asian, White + BA/BS, White + No BA/BS, Republican, Democrat, Independent, and 65+) as the columns and their 
respective values as the row. Using these dataframes, we were able to create visuals that allowed us to analyze the data and 
look into the problem described above.


# Datasets Used
- Exit poll data pulled from Edison Research through the avenues of CNN and the New York Times
- Pre-election polling data derived from many pollsters. Marist, Monmouth, and Siena make up the A+, phone pollsters.
Emerson (A- rating) is the only mixed (online,phone, and text) pollster and SurveyMonkey is the only completely online pollster 
- Difference/delta between Biden and Trump's support from their respective supporters between the pre-election polls and exit polls
- Presidential and senate election official results by party


# How to Execute the Code
In order to run the project, open the 2020ElectionAnalysis.ipynb, 2020ElectionAnalysis_Visuals_Bar_Radar_Charts.ipynb,
2020ElectionAnalysis_Visuals_Maps.ipynb Jupyter Notebooks and run all the cells within those notebooks.

2020ElectionAnalysis.ipynb is the notebook in which one can see the data being processed into usable dataframes. 
2020ElectionAnalysis_Visuals_Bar_Radar_Charts.ipynb is the notebook that utilizes the dataframes created to form and plot bar and radar charts.
2020ElectionAnalysis_Visuals_Maps.ipynb is the notebook in which the chloropleth maps can be formed and seen.

NOTE: ALL FILE PATHS ARE RELATIVE TO THOSE IN GIT REPO. Within the .py files, the variable, "base," may need to be changed to change the base data directory
to run the code. If there are any troubles with running the code or notebooks, please reach out to any of the group members.

# Files Contained
- The processing.py file contains utility functions that are imported to the notebook to keep it presentable.
Please keep in mind the functionality is dependent on the directory layout.
- 2020 Election Analysis Notebook: demonstrates the processing functions within processing.py in action
- visuals_bar_radar_chart.py: This holds the functions used for processing the dataframes in a way such that it is feasible to plot bar and radar charts.
- visuals_maps.py: This holds functions used to process dataframes and plot chloropleth maps.
- 2020 Election Analysis Visuals (Bar and Radar Charts) Notebook
- 2020 Election Analysis Visuals (Maps) Notebook
- data folder: holds all the datasets utilized for this project
- PDF of Presentation
- PDF of Project Proposal
- Assignment 3 Test Cases

# Libraries and Modules Used
The user should import all the libraries listed below to run the notebooks
Libraries: functools, json, matplotlib.pyplot, numpy, os, pandas, and plotly

