# ECE143 Team 8
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
demographics specified in the exit polling data.

# Datasets Used
- Exit poll data pulled from Edison Research through the avenues of CNN and the New York Times
- Pre-election polling data derived from many pollsters. Marist, Monmouth, and Siena make up the A+, phone pollsters.
Emerson (A- rating) is the only mixed (online,phone, and text) pollster and SurveyMonkey is the only completely online pollster 
- Difference/delta between Biden and Trump's support from their respective supporters between the pre-election polls and exit polls
- Presidential and senate election official results


# How to Execute the Code
In order to run the project, open the 2020ElectionAnalysis.ipynb, 2020ElectionAnalysis_Visuals_Bar_Radar_Charts.ipynb,
2020ElectionAnalysis_Visuals_Maps.ipynb Jupyter Notebooks and run all the cells within those notebooks.

# Files Contained
- The processing.py file contains utility functions that are imported to the notebook to keep it presentable.
Please keep in mind the functionality is dependent on the directory layout.
- 2020 Election Analysis Notebook: demonstrates the processing functions within processing.py in action
- visuals_bar_radar_chart.py: This holds the functions used for processing the dataframes in a way such that it is feasible to plot bar and radar charts
- visuals_maps.py: This holds functions used to process dataframes and plot chloropleth maps.
- 2020 Election Analysis Visuals (Bar and Radar Charts) Notebook
- 2020 Election Analysis Visuals (Maps) Notebook
- data folder: holds all the datasets utilized for this project
- PDF of Presentation
- PDF of Project Proposal

# Libraries Used
The user should import all the libraries listed below to run the notebooks
Libraries: functools, json, matplotlib.pyplot, numpy, os, pandas, and plotly

