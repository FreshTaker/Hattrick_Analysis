#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Filename: Entry.py
    Description: Script retireves CSV export from game, 
    analyzes the players in every possible position, 
    and exports data in an excel file.
    Author: Paul Brockmann
"""

import tkinter
from tkinter.filedialog import askopenfilename
import pandas as pd
import random
import matplotlib.pyplot as plt
from statistics import mean, quantiles


def select_csv_file():
    """Select CSV File"""
    global INPUT_DIR
    tkinter.Tk().withdraw() # Close the root window
    INPUT_DIR = askopenfilename()
    print(INPUT_DIR)


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
        CD = 0.87 * float(p['Keeper']) + 0.35 * float(p['Defending'])
        SD = 0.61 * float(p['Keeper']) + 0.25 * float(p['Defending'])
        
    if position == 'CCD':
        #Center Central Defender
        SD = 0.26 * float(p['Defending'])
        CD = 1.0 * float(p['Defending'])
        MID = 0.25 * float(p['Playmaking'])
        
    if position == 'CLRD':
        #Left/right Central Defender
        SD = 0.52 * float(p['Defending'])
        CD = 1.0 * float(p['Defending'])
        MID = 0.25 * float(p['Playmaking'])
        
    if position == 'CDW':
        #Central Defender with Wing Focus
        SD = 0.81 * float(p['Defending'])
        CD = 0.67 * float(p['Defending'])
        MID = 0.15 * float(p['Playmaking'])
        SA = 0.26 * float(p['Winger'])
        
    if position == 'CDO':
        #Central Defender with Off. Focus
        SD = 0.20 * float(p['Defending'])
        CD = 0.40 * float(p['Defending'])
        MID = 0.73 * float(p['Playmaking'])
        SA = 0.40 * float(p['Winger'])       
    
    if position == 'WBD':
        #Wingback with Def focus
        SD = 1.0 * float(p['Defending'])
        CD = 0.43 * float(p['Defending'])
        MID = 0.10 * float(p['Playmaking'])
        SA = 0.45 * float(p['Winger'])
    
    if position == 'WB':
        #Wingback
        SD = 0.92 * float(p['Defending'])
        CD = 0.38 * float(p['Defending'])
        MID = 0.15 * float(p['Playmaking'])
        SA = 0.59 * float(p['Winger'])
        
    if position == 'WBM':
        #Wingback with Mid Focus
        SD = 0.75 * float(p['Defending'])
        CD = 0.70 * float(p['Defending'])
        MID = 0.20 * float(p['Playmaking'])
        SA = 0.39 * float(p['Winger'])
        
    if position == 'WBO':
        #Wingback with Off Focus
        SD = 0.74 * float(p['Defending'])
        CD = 0.35 * float(p['Defending'])
        MID = 0.20 * float(p['Playmaking'])
        SA = 0.69 * float(p['Winger'])
        
    if position == 'WD':
        #Winger with Def Focus
        SD = 0.61 * float(p['Defending'])
        CD = 0.25 * float(p['Defending'])
        MID = 0.30 *float(p['Playmaking'])
        SA = 0.69 *float(p['Winger']) + 0.21* float(p['Passing'])
        CA = 0.05*float(p['Passing'])
    
    if position == 'W':
        #Winger
        SD = 0.35 * float(p['Defending'])
        CD = 0.20 * float(p['Defending'])
        MID = 0.45 *float(p['Playmaking'])
        SA = 0.86 *float(p['Winger']) + 0.26 * float(p['Passing'])
        CA = 0.11*float(p['Passing'])
        
    if position == 'WM':
        #Winger wih Mid Focus
        SD = 0.29 * float(p['Defending'])
        CD = 0.25 * float(p['Defending'])
        MID = 0.55 *float(p['Playmaking'])
        SA = 0.74 *float(p['Winger']) + 0.15 * float(p['Passing'])
        CA = 0.16*float(p['Passing'])
        
    if position == 'WO':
        #Winger with Off Focus
        SD = 0.22 * float(p['Defending'])
        CD = 0.13 * float(p['Defending'])
        MID = 0.30 * float(p['Playmaking'])
        SA = 0.100 * float(p['Winger']) + 0.29 * float(p['Passing'])
        CA = 0.13 * float(p['Passing'])
    
    if position == 'ICMD':
        #Inner Center Midfielder with Def Focus
        SD = 0.14 * float(p['Defending'])
        CD = 0.58 * float(p['Defending'])
        MID = 0.95 *float(p['Playmaking'])
        SA = 0.07 * float(p['Passing'])
        CA = 0.18 * float(p['Passing']) + 0.13 * float(p['Scoring'])
    
    if position == 'ILRMD':
        #Inner L/R Midfielder with Def. Focus
        SD = 0.27 * float(p['Defending'])
        CD = 0.58 * float(p['Defending'])
        MID = 0.95 * float(p['Playmaking'])
        SA = 0.14 * float(p['Passing'])
        CA = 0.18 * float(p['Passing']) + 0.13*float(p['Scoring'])
    
    if position == 'ICM':
        #Inner Central Midfielder
        SD = 0.09 * float(p['Defending'])
        CD = 0.40 * float(p['Defending'])
        MID = 1.0 * float(p['Playmaking'])
        SA = 0.13 * float(p['Passing'])
        CA = 0.33 * float(p['Passing']) + 0.22*float(p['Scoring'])
    
    if position == 'ILRM':
        #Inner L/R Midfielder
        SD = 0.19 * float(p['Defending'])
        CD = 0.40 * float(p['Defending'])
        MID = 1.0 * float(p['Playmaking'])
        SA = 0.26 * float(p['Passing'])
        CA = 0.33 * float(p['Passing']) + 0.22 * float(p['Scoring'])
    
    if position == 'IMW':
        #Inner Midfielder w/ Winger Focus
        SD = 0.24 * float(p['Defending'])
        CD = 0.33 * float(p['Defending'])
        MID = 0.9 * float(p['Playmaking'])
        SA = 0.31 * float(p['Passing']) + 0.59 * float(p['Winger'])
        CA = 0.23 * float(p['Passing'])
        
    if position == 'ICMO':
        #Inner Central Midfielder w/ Off. Focus
        SD = 0.04 * float(p['Defending'])
        CD = 0.16 * float(p['Defending'])
        MID = 0.95 * float(p['Playmaking'])
        SA = 0.18 * float(p['Passing'])
        CA = 0.49 * float(p['Passing']) + 0.31 * float(p['Scoring'])
    
    if position == 'ILRMO':
        #Inner L/R Midfielder w/ Off. Focus
        SD = 0.09 * float(p['Defending'])
        CD = 0.16 * float(p['Defending'])
        MID = 0.95 * float(p['Playmaking'])
        SA = 0.36 * float(p['Passing'])
        CA = 0.49 * float(p['Passing']) + 0.31 * float(p['Scoring'])
        
    if position == 'FWD':
        #Forward with Def. Focus
        SA = 0.13*float(p['Scoring']) + 0.14 * float(p['Winger']) + 0.31 * float(p['Passing'])
        CA = 0.56*float(p['Scoring']) + 0.53 * float(p['Passing'])
        MID = 0.35*float(p['Playmaking'])
    
    if position == 'FW':
        #Forward
        SA = 0.221 * float(p['Scoring'])+0.18 * float(p['Winger']) + 0.121 * float(p['Passing'])
        CA = 1.0 * float(p['Scoring']) + 0.369 * float(p['Passing'])
        MID = 0.25 * float(p['Playmaking'])
        
    if position == 'FWW':
        #Forward with Winger Focus
        SA = 0.51 * float(p['Scoring'])+0.64 * float(p['Winger']) + 0.21 * float(p['Passing'])
        CA = 0.66 * float(p['Scoring'])+0.23 * float(p['Passing'])
        MID = 0.15 * float(p['Playmaking'])
        #***something might be missing here***
        
    if position == 'FWD':
        #Forward with Def. Focus
        SA = 0.13 * float(p['Scoring']) + 0.13 * float(p['Winger']) + 0.41 * float(p['Passing'])
        CA = 0.56 * float(p['Scoring']) + 0.53 * float(p['Passing'])
        MID = 0.35 * float(p['Playmaking'])
    
    return [CD, SD, MID, SA, CA]

def topSpots():
    pos_positions = ['GK', 'CCD', 'CLRD', 'CDW', 'CDO', 'WBD', 'WB', 'WBM', 'WBO', 'WD', 'W', 'WM', 'WO', 'ICMD', 'ILRMD', 'ICM', 'ILRM', 'IMW', 'ICMO', 'ILRMO', 'FWD', 'FW', 'FWW', 'FWD']
    df_names = df0['Name']
    for g in df_names:
        for i in pos_positions:
            a = player_contrib(g, i)
            sum_a = 0
            for n in a:
                sum_a = sum_a+n
            a.append(sum_a)
            if i == 'GK':
                dict1 = {i:a}
            else:
                dict1[i] = a
        df1=pd.DataFrame(dict1)
        df1=df1.tail(1)
        df1=pd.melt(df1)
        result = df1.nlargest(5, 'value')
        return result


def topspotsdf(integer, DF, DF0):
    """ Organizes the data and selects the top positions of each player."""
    pos_positions = ['GK', 'CCD', 'CLRD', 'CDW', 'CDO', 'WBD', 'WB', 'WBM', 'WBO', 'WD', 'W', 'WM', 'WO', 'ICMD', 'ILRMD', 'ICM', 'ILRM', 'IMW', 'ICMO', 'ILRMO', 'FWD', 'FW', 'FWW', 'FWD']
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
    return result_df


def result_df_sort(DF, DF0):
    """ Function to sort result_df from topspotsdf()."""
    print('result_df_sort() needs more work')
    #Add Player's last position right below name
    try:
        df_names = DF0['Name']
        dict2 = {'POS': 'LAST'}
        for i in df_names:
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


def format_roster(DF, formation):
    """
    Cleans up dataframe by removing the coach, GKs, and trainees.
    Maintains the formation list.

    DF starts with players names as columns, rows are 0 - 22
    """
    DF = DF.set_index(['POS'])
    DF = DF.transpose()

    # Remove Coach?
    coach = 'Rogelio Nakamura'
    drop_coach = input(f'Should Coach {coach}, be dropped? (y/n): ')
    if drop_coach.lower() == "y":
        print('Dropping Coach')
        try:
            DF = DF.drop(coach)
            print('Successful dropping.')
        except KeyError:
            print('Coach not found. Please fix.')
    else:
        print('Coach not dropped.')
    print('Whole Team Roster:')
    print(DF)

    # Remove GKs?
    goalkeepers = ['Jack McCray', 'Phil Peeples']
    drop_goalkeepers = input(f'Should the goalkeepers, \n{goalkeepers}, \nbe dropped? (y,n): ')
    if drop_goalkeepers.lower() == 'y':
        try:
            formation.remove('GK')  #only one in formation
            for player in goalkeepers:
                DF = DF.drop(player)
                print(f'Dropped {player} (Goalkeeper)')
        except Exception as e:
            print(e)
    else:
        print('Goalkeepers are not dropped.')

    # Remove Trainees?
    trainees = ['Leopold Vach', 'Daniele Passarin', 'Sergiusz Soplica', 'Samuele Camaiani', 'Giovanni Plazas',
                'Yuanfu Fu', 'František Panec', 'Andrei Dochioiu', 'Detlef Wetter', 'Achikam Givon']
    training_positions = ['W', 'WB']
    drop_trainees = input(f'Should the {len(trainees)} trainees for {training_positions} be dropped? (y,n): ')
    if drop_trainees.lower() == 'y':
        try:
            for position in training_positions:
                for n in range(formation.count(position)):
                    formation.remove(position)
            for player in trainees:
                DF = DF.drop(player)
                print(f'Dropped {player} (Trainnee)')
        except Exception as e:
            print(e)
    else:
        print('Trainees are not dropped.')
    print(f'Formation = {formation}')
    return DF, formation


def random_lineup(DF, formation):
    """create random 11 person lineup
    starting with 4-4-2 layout (DEF, MID, FW + assumed GK)
    (1xGK, 2xFW, 2xILRM, 2xW, 2xWB, 2xCLRD)
    lineup_dict = {players_name, position}
    DF is Positions as columns, Names as rows
    """
    #formation = ['FW', 'FW', 'ILRM', 'ILRM', 'CLRD', 'CLRD']
    # Removed GK, W, W, WB, & WB
    spots = len(formation)

    players_index = []
    while spots >= 0:
        i = random.randint(0, len(DF)-1)
        if i not in players_index:
            players_index.append(i)
            spots -= 1
    lineup_dict = {}
    for players_i, position in zip(players_index, formation):
        lineup_dict[DF.iloc[players_i].name] = str(position)
    return lineup_dict, DF


def clean_DF(lineup_dict, DF):
    """Removes the players from in the lineup_dict from the DF"""
    for player in lineup_dict:
        DF = DF.drop(player)
    return DF


def determine_lineup_score(lineup_dict, DF):
    """Determine lineup score using scores in DF.
            lineup_dict = {players_name, position}
            DF is Positions as columns, Names as rows
    """
    #lineup_dict = {'Hossam Ayoub':'FW', 'Jack McCray':'GK' }
    score = 0
    for player in lineup_dict:
        position_score = DF.loc[player][lineup_dict[player]]
        if position_score == 'NaN':
            position_score = 0
        score += position_score
    score = round(score, 1)
    return score


def do_lineup_iterations(iterations, DF, formation):
    """Do number of iterations to find the best lineup.  Returns cleaned DF"""
    best_score = 0
    best_lineup = []
    best_cleaned_DF = 0
    score_history = []
    for i in range(iterations):
        lineup_dict, r_DF = random_lineup(DF, formation)
        score = determine_lineup_score(lineup_dict, DF)
        score_history.append(score)
        if score > best_score:
            best_score = score
            best_lineup = lineup_dict
            r_DF = clean_DF(lineup_dict, r_DF)
            best_cleaned_DF = r_DF
            print(score, lineup_dict)

        print(i, score)
    return best_cleaned_DF, best_lineup, best_score, score_history


def export_result_df(Filename, DF):
    DF.to_excel(Filename+'.xlsx')
    print('Exported')
    print('Check the folder')


def plot_iterations(score_history1, score_history2):
    """Plot iterations"""
    length_history = max(len(score_history1), len(score_history2))
    py_mean1 = mean(score_history1).item()
    py_mean2 = mean(score_history2).item()
    print(py_mean1, py_mean2)
    quart1 = quantiles(score_history1, n=4)
    quart2 = quantiles(score_history2, n=4)
    print(quart1)
    print(quart2)
    x = list(range(1, length_history+1))
    x1 = list(range(1, len(score_history1)+1))
    x2 = list(range(1, len(score_history2)+1))
    average1 = [py_mean1] * length_history
    average2 = [py_mean2] * length_history
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #ax.scatter(x1, score_history1, color='red', marker='*', label='1st Line')
    #ax.scatter(x2, score_history2, color='blue', marker='x', label='2nd Line')
    ax.plot(x, average1, color='red', linewidth=2, label='1st Line Avg')
    ax.plot(x, average2, color='blue', linewidth=2, label='2st Line Avg')
    ax.plot(x, [quart1[0]]*length_history, color='red', linewidth=3, dashes=[5, 2, 1, 2])
    ax.plot(x, [quart1[1]]*length_history, color='red', linewidth=1, dashes=[5, 2, 1, 2])
    ax.plot(x, [quart1[2]]*length_history, color='red', linewidth=1, dashes=[5, 2, 1, 2])
    ax.plot(x, [quart2[0]]*length_history, color='blue', linewidth=1, dashes=[5, 2, 1, 2])
    ax.plot(x, [quart2[1]]*length_history, color='blue', linewidth=1, dashes=[5, 2, 1, 2])
    ax.plot(x, [quart2[2]]*length_history, color='blue', linewidth=1, dashes=[5, 2, 1, 2])
    ax.legend()
    ax.grid(True)
    ax.set(title='Lineup Comparison',
           ylabel='Score',
           xlabel='iterations')
    figure_name = 'iteration_history.png'
    plt.savefig(figure_name)
    print(f'Plot Created and saved as {figure_name}')


if __name__ == "__main__":
    select_csv_file()
    df, df0 = read_using_pd()
    df = topspotsdf(23, df, df0) #Enter in how many top spots
    df = result_df_sort(df, df0) #Needs work
    formation = ['GK', 'W', 'W', 'WB', 'WB', 'FW', 'FW', 'ILRM', 'ILRM', 'CLRD', 'CLRD'] #Should be 11
    df_by_names, formation = format_roster(df, formation)
    df_by_names2, lineup1, score1, score_history1 = do_lineup_iterations(100000, df_by_names, formation)
    df_by_names3, lineup2, score2, score_history2 = do_lineup_iterations(2000, df_by_names2, formation)
    print(f'Score for the First Lineup: {score1}')
    print(lineup1)
    print(f'Score for the Second Lineup: {score2}')
    print(lineup2)
    print(df_by_names3)
    plot_iterations(score_history1, score_history2)

    x = input('Do you want to export file? y/n:  ')
    if x == 'y':
        export_result_df('Team_Results', df)
        print('Exported results')
    else:
        print('Did not export results')
