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
    df = pd.read_csv(INPUT_DIR, skiprows=0)
    print(df.columns.tolist())

def analyze_pd():
    print(empty)
#ensure data types for columns are correct
#do calculations for the 18 positions
#run optimization routine (series of equations)
# with and without assigned training
#print best layout

def plot_pd():
    df.plot.bar(x='Experience',y='Name')
               
if __name__ == "__main__":
    main()
    read_using_pd()
    analyze_pd()
    plot_pd()


