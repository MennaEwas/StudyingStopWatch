"""
Studying stopwatch 
using oop paradigm 
still working on the GUI interface
Put sound in ring
"""
import time 
import sys 
from tkinter import *
import pandas as pd 
import csv 

class StopWatch:
    def __init__(self, ring):
        self.ring = ring #duration of each session in hrs 
        self.day = 0 
        self.hour = 0 
        self.minute = 0 
        self.second = 0 
        self.session = 0
        self.Time = ''
        
    def write_recording(self, session, time): #used inside
        with open('StopWatch.csv', 'w') as csvfile:
            fieldnames = ['Session', 'Time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Session': session, 'Time': time})
            
        
    def start(self): 
        running = True
        while running: 
            time.sleep(1) #delay execution 
            if self.second == 59: 
                self.second = -1 
                self.minute += 1
            self.second += 1 
            
            if self.minute == 59:
                self.minute = -1 
                self.hour += 1 
                
            
            if self.hour == 24:
                self.hour = -1 
                self.day += 1 
            
            #print(self.day, ":", self.hour, ":", self.minute, ":", self.second)
            self.Time = '{}d :{}h : {}m: {}s'.format(self.day,self.hour,self.minute,self.second)
            print(self.Time)
            
            if self.hour == self.ring:
                print("You passed it safely!")
                self.session += 1
                self.write_recording(self.session, self.time)
                running = False
                
            

    def summ(self): #how many hours you did in before reset
        summation = self.session * self.ring
        print('Until now you did:', summation)
    
    
    def reset(self):
        self.ring = 0 
        self.day = 0 
        self.hour = 0 
        self.minute = 0 
        self.second = 0 
        self.session = 0
        
    def Best_Record(self): 
        Data = pd.read_csv("StopWatch.csv") #read the data from csv file 
        Best = Data["Time"].max()
        if self.day == 1:
            print(Best)
       
   
    def display(self):
       self.start()
       self.summ() 
       if self.day == 1: 
           self.Best_Record()
           self.reset()
       

menna = StopWatch(5)
menna.display()

    
    
    
    
