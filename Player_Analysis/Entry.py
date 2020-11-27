#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Filename: Entry.py
    Description: Script retireves CSV export from game, 
    analyzes the players in every possible position, 
    and exports data in an excel file.
    Author: Paul Brockmann
"""

import csv
import tkinter
from tkinter.filedialog import askopenfilename
import pandas as pd

def main():
    """Select CSV File"""
    global INPUT_DIR
    tkinter.Tk().withdraw() # Close the root window
    INPUT_DIR = askopenfilename()
    print(INPUT_DIR)
    
def load_csv():
    """Load CSV file"""
    with open(INPUT_DIR,newline='',encoding='utf-8') as csvfile:
        print(csv.list_dialects())
        reader = csv.reader(csvfile, dialect='excel')
        for row in reader:
            print(row)


def read_using_pd():
    """Format data from CSV and load into Panda"""
    df = pd.read_csv(INPUT_DIR, skiprows=0, index_col='Name')
    df0 = pd.read_csv(INPUT_DIR, skiprows=0)
    print(df.columns.tolist())
    return df, df0

    
def player_contrib(name, position):
    """ Function that outputs the player's rating for that particular
    position.
    Reference: https://prnt.sc/mn7guu
    Reference: https://wiki.hattrick.org/wiki/Skill_contribution
    """
    position = position.upper() #formats inputs
    p = df.loc[name] #allows float(p['Keeper']) to be called
    f = 'float64'
    df.astype({'Keeper':f, 'Defending':f, 'Playmaking':f, 'Winger':f, 'Passing':f, 'Scoring':f})
    #position List:
    #[GK, CCD, CLRD, CDW, CDO, WBD, WB, WBM, WBO, WD, W, WM, WD, ICMD, ILRMD, ICM, ILRM, IMW, ICMO, ILRMO, FWD, FW, FWW, FWD]
    # GK = Goal Keeper
    # CCD = Center Central Defender
    # CLRD = Left/Right Central Defender
    # CDW = Central Defneder with Wing Focus
    # CDO = Central Defender with Off. Focus
    # WBD = Wingback with Def. Focus
    # WB = Wingback
    # WBM = Wingback with Mid. Focus
    # WBO = Wingback with Off. Focus
    # WD = Winger with Def. Focus
    # W = Winger
    # WM = Winger with Mid Focus
    # WD = Winger with Def. Focus
    # ICMD = Inner Center Midfielder with Def Focus
    # ILRMD = Inner L/R Midfielder with Def. Focus
    # ICM = Inner Cneteral Midfielder
    # ILRM = Inner L/R Midfielder
    # IMW = Inner Midfielder w/ Winger Focus
    # ICMO = Inner Central Midfielder w/ Off Focus
    # ILRMO = Inner L/R Midfielder w/ Off Focus
    # FWD = Foward w/ Def. Focus
    # FW = Forward
    # FWW = Forward with Winger Focus
    # FWD = Forward with Def. Focus    
    CD = 0; SD= 0; MID=0; SA=0; CA=0
    
    if position == 'GK':
        #Goal Keeper
        CD = 0.87*float(p['Keeper']) + 0.35*float(p['Defending'])
        SD = 0.61*float(p['Keeper']) + 0.25*float(p['Defending'])
        
    if position == 'CCD':
        #Center Central Defender
        SD = 0.26*float(p['Defending'])
        CD = 1.0*float(p['Defending'])
        MID = 0.25*float(p['Playmaking'])
        
    if position == 'CLRD':
        #Left/right Central Defender
        SD = 0.52*float(p['Defending'])
        CD = 1.0*float(p['Defending'])
        MID = 0.25*float(p['Playmaking'])
        
    if position == 'CDW':
        #Central Defender with Wing Focus
        SD = 0.81*float(p['Defending'])
        CD = 0.67*float(p['Defending'])
        MID = 0.15*float(p['Playmaking'])
        SA = 0.26 * float(p['Winger'])
        
    if position == 'CDO':
        #Central Defender with Off. Focus
        SD = 0.20*float(p['Defending'])
        CD = 0.40*float(p['Defending'])
        MID = 0.73*float(p['Playmaking'])
        SA = 0.40 * float(p['Winger'])       
    
    if position == 'WBD':
        #Wingback with Def focus
        SD = 1.0 * float(p['Defending'])
        CD = 0.43 * float(p['Defending'])
        MID = 0.10*float(p['Playmaking'])
        SA = 0.45 *float(p['Winger'])
    
    if position == 'WB':
        #Wingback
        SD = 0.92 * float(p['Defending'])
        CD = 0.38 * float(p['Defending'])
        MID = 0.15*float(p['Playmaking'])
        SA = 0.59 *float(p['Winger'])
        
    if position == 'WBM':
        #Wingback with Mid Focus
        SD = 0.75 * float(p['Defending'])
        CD = 0.70 * float(p['Defending'])
        MID = 0.20 *float(p['Playmaking'])
        SA = 0.39 *float(p['Winger'])
        
    if position == 'WBO':
        #Wingback with Off Focus
        SD = 0.74 * float(p['Defending'])
        CD = 0.35 * float(p['Defending'])
        MID = 0.20 *float(p['Playmaking'])
        SA = 0.69 *float(p['Winger'])
        
    if position == 'WD':
        #Winger with Def Focus
        SD = 0.61 * float(p['Defending'])
        CD = 0.25 * float(p['Defending'])
        MID = 0.30 *float(p['Playmaking'])
        SA = 0.69 *float(p['Winger']) + 0.21*float(p['Passing'])
        CA = 0.05*float(p['Passing'])
    
    if position == 'W':
        #Winger
        SD = 0.35 * float(p['Defending'])
        CD = 0.20 * float(p['Defending'])
        MID = 0.45 *float(p['Playmaking'])
        SA = 0.86 *float(p['Winger']) + 0.26*float(p['Passing'])
        CA = 0.11*float(p['Passing'])
        
    if position == 'WM':
        #Winger wih Mid Focus
        SD = 0.29 * float(p['Defending'])
        CD = 0.25 * float(p['Defending'])
        MID = 0.55 *float(p['Playmaking'])
        SA = 0.74 *float(p['Winger']) + 0.15*float(p['Passing'])
        CA = 0.16*float(p['Passing'])
        
    if position == 'WO':
        #Winger with Off Focus
        SD = 0.22 * float(p['Defending'])
        CD = 0.13 * float(p['Defending'])
        MID = 0.30 *float(p['Playmaking'])
        SA = 0.100 *float(p['Winger']) + 0.29*float(p['Passing'])
        CA = 0.13*float(p['Passing'])
    
    if position == 'ICMD':
        #Inner Center Midfielder with Def Focus
        SD = 0.14 * float(p['Defending'])
        CD = 0.58 * float(p['Defending'])
        MID = 0.95 *float(p['Playmaking'])
        SA = 0.07 *float(p['Passing'])
        CA = 0.18*float(p['Passing']) + 0.13*float(p['Scoring'])
    
    if position == 'ILRMD':
        #Inner L/R Midfielder with Def. Focus
        SD = 0.27 * float(p['Defending'])
        CD = 0.58 * float(p['Defending'])
        MID = 0.95 *float(p['Playmaking'])
        SA = 0.14 *float(p['Passing'])
        CA = 0.18*float(p['Passing']) + 0.13*float(p['Scoring'])
    
    if position == 'ICM':
        #Inner Central Midfielder
        SD = 0.09 * float(p['Defending'])
        CD = 0.40 * float(p['Defending'])
        MID = 1.0 *float(p['Playmaking'])
        SA = 0.13 *float(p['Passing'])
        CA = 0.33*float(p['Passing']) + 0.22*float(p['Scoring'])
    
    if position == 'ILRM':
        #Inner L/R Midfielder
        SD = 0.19 * float(p['Defending'])
        CD = 0.40 * float(p['Defending'])
        MID = 1.0 *float(p['Playmaking'])
        SA = 0.26 *float(p['Passing'])
        CA = 0.33*float(p['Passing']) + 0.22*float(p['Scoring'])
    
    if position == 'IMW':
        #Inner Midfielder w/ Winger Focus
        SD = 0.24 * float(p['Defending'])
        CD = 0.33 * float(p['Defending'])
        MID = 0.9 *float(p['Playmaking'])
        SA = 0.31 *float(p['Passing']) + 0.59 * float(p['Winger'])
        CA = 0.23*float(p['Passing'])
        
    if position == 'ICMO':
        #Inner Central Midfielder w/ Off. Focus
        SD = 0.04 * float(p['Defending'])
        CD = 0.16 * float(p['Defending'])
        MID = 0.95 *float(p['Playmaking'])
        SA = 0.18 *float(p['Passing'])
        CA = 0.49*float(p['Passing']) + 0.31*float(p['Scoring'])
    
    if position == 'ILRMO':
        #Inner L/R Midfielder w/ Off. Focus
        SD = 0.09 * float(p['Defending'])
        CD = 0.16 * float(p['Defending'])
        MID = 0.95 *float(p['Playmaking'])
        SA = 0.36 *float(p['Passing'])
        CA = 0.49*float(p['Passing']) + 0.31*float(p['Scoring'])
        
    if position == 'FWD':
        #Forward with Def. Focus
        SA = 0.13*float(p['Scoring']) + 0.14*float(p['Winger'])+0.31*float(p['Passing'])
        CA = 0.56*float(p['Scoring']) + 0.53*float(p['Passing'])
        MID = 0.35*float(p['Playmaking'])
    
    if position == 'FW':
        #Forward
        SA = 0.221*float(p['Scoring'])+0.18*float(p['Winger'])+0.121*float(p['Passing'])
        CA = 1.0*float(p['Scoring']) + 0.369*float(p['Passing'])
        MID = 0.25*float(p['Playmaking'])
        
    if position == 'FWW':
        #Forward with Winger Focus
        SA = 0.51*float(p['Scoring'])+0.64*float(p['Winger'])+0.21*float(p['Passing'])
        CA = 0.66*float(p['Scoring'])+0.23*float(p['Passing'])
        MID = 0.15*float(p['Playmaking'])
        #***something might be missing here***
        
    if position == 'FWD':
        #Forward with Def. Focus
        SA = 0.13*float(p['Scoring'])+0.13*float(p['Winger'])+0.41*float(p['Passing'])
        CA = 0.56*float(p['Scoring'])+0.53*float(p['Passing'])
        MID = 0.35*float(p['Playmaking'])
    
    return [CD, SD, MID, SA, CA]

def topSpots():
    pos_positions = ['GK', 'CCD', 'CLRD', 'CDW', 'CDO', 'WBD', 'WB', 'WBM', 'WBO', 'WD', 'W', 'WM', 'WD', 'ICMD', 'ILRMD', 'ICM', 'ILRM', 'IMW', 'ICMO', 'ILRMO', 'FWD', 'FW', 'FWW', 'FWD']
    df1_rows = ['POS','CD','SD','MID','SA','CA', 'SUM']
    
    #Need to filter out the Coach (use Coach Column)
    #test
    df_names = df0['Name']
    #df_names = df0.loc[df0['Coach'] != 1, ['Name']] #Select all the Names, but the one that is the Coach
    
    #print(df_names.size())
    # If having trouble iterating through the dataframe, see this:
    #  https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
    #  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.itertuples.html
   
    for g in df_names:
        for i in pos_positions:
            a = player_contrib(g, i)
            #a.append(i)
            sum_a = 0
            for n in a:
                sum_a = sum_a+n
            a.append(sum_a)
            if i == 'GK':
                dict1 = {i:a}
            else:
                dict1[i] = a
        df1=pd.DataFrame(dict1)
        #df1.iloc[5] #selecting just the sum
        df1=df1.tail(1)
        df1=pd.melt(df1)
        result = df1.nlargest(5,'value')
        #print(g)
        #print(result)


def topspotsdf(integer, DF, DF0):
    """ Organizes the data and selects the top positions of each player."""
    pos_positions = ['GK', 'CCD', 'CLRD', 'CDW', 'CDO', 'WBD', 'WB', 'WBM', 'WBO', 'WD', 'W', 'WM', 'WD', 'ICMD', 'ILRMD', 'ICM', 'ILRM', 'IMW', 'ICMO', 'ILRMO', 'FWD', 'FW', 'FWW', 'FWD']
    df1_rows = ['POS', 'CD', 'SD', 'MID', 'SA', 'CA', 'SUM']
    #result_df = DF
    df_names = DF0['Name']
    x = 0
    for g in df_names:
        for i in pos_positions:
            a = player_contrib(g, i)
            #a.append(i)
            sum_a = 0
            for n in a:
                sum_a = sum_a+n
            a.append(sum_a)
            if i == 'GK':
                dict1 = {i: a}
            else:
                dict1[i] = a
                
        #last_position = df0['Last match position']
        #df0.loc[df0['Name']==g,['Last match position']]
        df1 = pd.DataFrame(dict1)
        #df1.iloc[5] #selecting just the sum
        df1 = df1.tail(1) #selecting just the sum
        df1 = pd.melt(df1) #Columsn into Rows
        int_df = df1.nlargest(integer, 'value')
        int_df.columns = ['POS', g]
        if x == 0:
            x += 1
            result_df = int_df
        else:
            result_df = pd.merge(result_df, int_df, how='outer', on='POS')
    print(result_df)
    return result_df


def result_df_sort(DF, DF0):
    """ Function to sort result_df from topspotsdf()."""
    print('result_df_sort() needs more work')
    #Add Player's last position right below name
    try:
        print(DF['Hossam Ayoub'])
        print(DF0)
        df_names = DF0['Name']
        dict2 = {'POS': 'LAST'}
        for i in df_names:
            print(i)
            p = DF[i]#p = DF.loc[i]
            last_pos = p['Last match position']
            dict2[i] = last_pos
        df2 = pd.DataFrame(data=dict2, index=[22])
        result_df2 = pd.concat([DF, df2], sort=False)
    except Exception as e:
        print(e)
        result_df2 = DF
    #Add Player's age
    return result_df2


def select_starting_roster(DF):
    """DF starts with players names as columns, rows are 0 - 22"""
    print('Dropping Coach')
    Coach = 'Rogelio Nakamura'
    try:
        DF = DF.drop(Coach)
        print('Successful dropping.')
        # DF.dtypes
    except KeyError:
        print('Coach not found. Please fix.')

    DF = DF.set_index(['POS'])
    DF = DF.transpose()
    print(DF)
    # Find best GK:
    print(DF.sort_values('GK', ascending=False).head(2))

    #print(DF.loc['Hossam Ayoub']['FW']) gets score

    #Need to add more

    return DF


def determine_lineup_score(lineup_dict, DF):
    """Determine lineup score using scores in DF.
            lineup_dict = {players_name, position}
            DF is Positions as columns, Names as rows
    """
    lineup_dict = {'Hossam Ayoub':'FW', 'Jack McCray':'GK' }
    score = 0
    for player in lineup_dict:
        position_score = DF.loc[player][lineup_dict[player]]
        score += position_score
        
    print(score)
    return score

def export_result_df(Filename, DF):
    DF.to_excel(Filename+'.xlsx')
    print('Exported')
    print('Check the folder')


def plot_pd():
    #df.plot.bar(x='Experience',y='Name')
    print('No plot to see here')


if __name__ == "__main__":
    main()
    df, df0 = read_using_pd()
    plot_pd()
    df = topspotsdf(22, df, df0) #Enter in how many top spots
    df = result_df_sort(df, df0) #Needs work
    df_by_names = select_starting_roster(df)
    determine_lineup_score({}, df_by_names)

    x = input('Do you want to export file? y/n:  ')
    if x == 'y':
        export_result_df('Team_Results', df)
    else:
        print("That's okay")

    
