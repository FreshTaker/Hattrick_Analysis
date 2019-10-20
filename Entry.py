# Read CSV file for analysis

# Made need Firefox
import os
import csv
import tkinter
import matplotlib
from tkinter.filedialog import askopenfilename
import pandas as pd

def main():
    global INPUT_DIR
    tkinter.Tk().withdraw() # Close the root window
    INPUT_DIR = askopenfilename()
    print(INPUT_DIR)
    
def load_csv():
    with open(INPUT_DIR,newline='',encoding='utf-8') as csvfile:
        print(csv.list_dialects())
        reader = csv.reader(csvfile, dialect='excel')
        for row in reader:
            print(row)
            
def read_using_pd():
    global df #dataframe
    df = pd.read_csv(INPUT_DIR, skiprows=0, index_col='Name')
    print(df.columns.tolist())

def analyze_pd():
    print(' ')
    df.dtypes
    
def player_contrib(name, position):
    #this is to plug in the player's name and position to get the
    #impact the player has on the team.
    #reference: https://prnt.sc/mn7guu
    #reference: https://wiki.hattrick.org/wiki/Skill_contribution
    
    position = position.upper() #formats inputs
    
    p = df.loc[name] #allows p['Keeper'] to be called
    
    #position List:
    #[GK, CDD, CLRD, CDW, CDO, WBD, WB, WBM, WBO, WD, W, WM, WD, ICMD, ILRMD, ICM, ILRM, IMW, ICMO, ILRMO, FWD, FW, FWW, FWD]
    # GK = Goal Keeper
    # CDD = Center Central Defender
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
        CD = 0.87*p['Keeper'] + 0.35*p['Defending']
        SD = 0.61*p['Keeper'] + 0.25*p['Defending']
        
    if position == 'CCD':
        #Center Central Defender
        SD = 0.26*p['Defending']
        CD = 1.0*p['Defending']
        MID = 0.25*p['Playmaking']
        
    if position == 'CLRD':
        #Left/right Central Defender
        SD = 0.52*p['Defending']
        CD = 1.0*p['Defending']
        MID = 0.25*p['Playmaking']
        
    if position == 'CDW':
        #Central Defender with Wing Focus
        SD = 0.81*p['Defending']
        CD = 0.67*p['Defending']
        MID = 0.15*p['Playmaking']
        SA = 0.26 * p['Winger']
        
    if position == 'CDO':
        #Central Defender with Off. Focus
        SD = 0.20*p['Defending']
        CD = 0.40*p['Defending']
        MID = 0.73*p['Playmaking']
        SA = 0.40 * p['Winger']       
    
    if position == 'WBD':
        #Wingback with Def focus
        SD = 1.0 * p['Defending']
        CD = 0.43 * p['Defending']
        MID = 0.10*p['Playmaking']
        SA = 0.45 *p['Winger']
    
    if position == 'WB':
        #Wingback
        SD = 0.92 * p['Defending']
        CD = 0.38 * p['Defending']
        MID = 0.15*p['Playmaking']
        SA = 0.59 *p['Winger']
        
    if position == 'WBM':
        #Wingback with Mid Focus
        SD = 0.75 * p['Defending']
        CD = 0.70 * p['Defending']
        MID = 0.20 *p['Playmaking']
        SA = 0.39 *p['Winger']
        
    if position == 'WBO':
        #Wingback with Off Focus
        SD = 0.74 * p['Defending']
        CD = 0.35 * p['Defending']
        MID = 0.20 *p['Playmaking']
        SA = 0.69 *p['Winger']
        
    if position == 'WD':
        #Winger with Def Focus
        SD = 0.61 * p['Defending']
        CD = 0.25 * p['Defending']
        MID = 0.30 *p['Playmaking']
        SA = 0.69 *p['Winger'] + 0.21*p['Passing']
        CA = 0.05*p['Passing']
    
    if position == 'W':
        #Winger
        SD = 0.35 * p['Defending']
        CD = 0.20 * p['Defending']
        MID = 0.45 *p['Playmaking']
        SA = 0.86 *p['Winger'] + 0.26*p['Passing']
        CA = 0.11*p['Passing']
        
    if position == 'WM':
        #Winger wih Mid Focus
        SD = 0.29 * p['Defending']
        CD = 0.25 * p['Defending']
        MID = 0.55 *p['Playmaking']
        SA = 0.74 *p['Winger'] + 0.15*p['Passing']
        CA = 0.16*p['Passing']
        
    if position == 'WO':
        #Winger with Off Focus
        SD = 0.22 * p['Defending']
        CD = 0.13 * p['Defending']
        MID = 0.30 *p['Playmaking']
        SA = 0.100 *p['Winger'] + 0.29*p['Passing']
        CA = 0.13*p['Passing']
    
    if position == 'ICMD':
        #Inner Center Midfielder with Def Focus
        SD = 0.14 * p['Defending']
        CD = 0.58 * p['Defending']
        MID = 0.95 *p['Playmaking']
        SA = 0.07 *p['Passing']
        CA = 0.18*p['Passing'] + 0.13*p['Scoring']
    
    if position == 'ILRMD':
        #Inner L/R Midfielder with Def. Focus
        SD = 0.27 * p['Defending']
        CD = 0.58 * p['Defending']
        MID = 0.95 *p['Playmaking']
        SA = 0.14 *p['Passing']
        CA = 0.18*p['Passing'] + 0.13*p['Scoring']
    
    if position == 'ICM':
        #Inner Central Midfielder
        SD = 0.09 * p['Defending']
        CD = 0.40 * p['Defending']
        MID = 1.0 *p['Playmaking']
        SA = 0.13 *p['Passing']
        CA = 0.33*p['Passing'] + 0.22*p['Scoring']
    
    if position == 'ILRM':
        #Inner L/R Midfielder
        SD = 0.19 * p['Defending']
        CD = 0.40 * p['Defending']
        MID = 1.0 *p['Playmaking']
        SA = 0.26 *p['Passing']
        CA = 0.33*p['Passing'] + 0.22*p['Scoring']
    
    if position == 'IMW':
        #Inner Midfielder w/ Winger Focus
        SD = 0.24 * p['Defending']
        CD = 0.33 * p['Defending']
        MID = 0.9 *p['Playmaking']
        SA = 0.31 *p['Passing'] + 0.59 * p['Winger']
        CA = 0.23*p['Passing']
        
    if position == 'ICMO':
        #Inner Central Midfielder w/ Off. Focus
        SD = 0.04 * p['Defending']
        CD = 0.16 * p['Defending']
        MID = 0.95 *p['Playmaking']
        SA = 0.18 *p['Passing']
        CA = 0.49*p['Passing'] + 0.31*p['Scoring']
    
    if position == 'ILRMO':
        #Inner L/R Midfielder w/ Off. Focus
        SD = 0.09 * p['Defending']
        CD = 0.16 * p['Defending']
        MID = 0.95 *p['Playmaking']
        SA = 0.36 *p['Passing']
        CA = 0.49*p['Passing'] + 0.31*p['Scoring']
        
    if position == 'FWD':
        #Forward with Def. Focus
        SA = 0.13*p['Scoring'] + 0.14*p['Winger']+0.31*p['Passing']
        CA = 0.56*p['Scoring'] + 0.53*p['Passing']
        MID = 0.35*p['Playmaking']
    
    if position == 'FW':
        #Forward
        SA = 0.221*p['Scoring']+0.18*p['Winger']+0.121*p['Passing']
        CA = 1.0*p['Scoring'] + 0.369*p['Passing']
        MID = 0.25*p['Playmaking']
        
    if position == 'FWW':
        #Forward with Winger Focus
        SA = 0.51*p['Scoring']+0.64*p['Winger']+0.21*p['Passing']
        CA = 0.66*p['Scoring']+0.23*p['Passing']
        MID = 0.15*p['Playmaking']
        #***something might be missing here***
        
    if position == 'FWD':
        #Forward with Def. Focus
        SA = 0.13*p['Scoring']+0.13*p['Winger']+0.41*p['Passing']
        CA = 0.56*p['Scoring']+0.53*p['Passing']
        MID = 0.35*p['Playmaking']
    
    return [CD, SD, MID, SA, CA]

#ensure data types for columns are correct
#do calculations for the 18 positions
#run optimization routine (series of equations)
# with and without assigned training
#print best layout

#1) Analyze all team members for all positions.
#2) Assign players based on optimal positions, eliminated those taken
#3) Make a short hand print out or CSV listing player with position.

def plot_pd():
    #df.plot.bar(x='Experience',y='Name')
    print('No plot to see here')
if __name__ == "__main__":
    main()
    read_using_pd()
    analyze_pd()
    plot_pd()
    a = player_contrib('Austin Sanders','GK')
    print(a)
    
    pos_positions = ['GK', 'CDD', 'CLRD', 'CDW', 'CDO', 'WBD', 'WB', 'WBM', 'WBO', 'WD', 'W', 'WM', 'WD', 'ICMD', 'ILRMD', 'ICM', 'ILRM', 'IMW', 'ICMO', 'ILRMO', 'FWD', 'FW', 'FWW', 'FWD']
    df1_columns = ['CD','SD','MID','SA','CA','POS']
                     
    for i in pos_positions:
        a = player_contrib('Austin Sanders',i)
        a.append(i)
        if i == 'GK':
            df1 = pd.DataFrame(a)
        else:
            df1 = pd.merge(df1, pd.DataFrame(a), how='outer', on=0)
    
    print('done')

                
            
            
        
        
        
        
        

        




