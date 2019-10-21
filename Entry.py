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

def top5spots():
    pos_positions = ['GK', 'CCD', 'CLRD', 'CDW', 'CDO', 'WBD', 'WB', 'WBM', 'WBO', 'WD', 'W', 'WM', 'WD', 'ICMD', 'ILRMD', 'ICM', 'ILRM', 'IMW', 'ICMO', 'ILRMO', 'FWD', 'FW', 'FWW', 'FWD']
    df1_rows = ['POS','CD','SD','MID','SA','CA', 'SUM']
    df_names = ['Leider Moncada', 'Stuart Bates']
    
    for g in df_names:
        for i in pos_positions:
            a = player_contrib(g,i)
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
        print(g)
        print(result)
    


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
            df1 = pd.DataFrame(a)
    top5spots()
    
 
                
            
            
        
        
        
        
        

        




