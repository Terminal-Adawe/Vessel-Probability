#!/usr/bin/env python
# Import necessary python modules and packages
from tkinter import *
from tkinter import messagebox
import random
import numpy as np
import matplotlib.pyplot as plt
import itertools

plt.rcParams.update({'font.size': 22})
def randomBlocks(days,ast,nvc):
    randList=[]
    for i in range(nvc):
        randList.append(random.randrange(1,np.ceil(days*24/ast)))
    return np.array(randList)

def tally(lst):
    #tallyList=np.bincount(lst)
    #nonZeroIndices=np.nonzero(tallyList)[0]
    #return np.transpose([nonZeroIndices,tallyList[nonZeroIndices]])
    return np.bincount(lst)

#def count(lst):
#    if (len(lst.shape)==1):
#        countList=tally(np.transpose(tally(lst))[1])
#    elif (len(lst.shape)==2):
#        countList=tally(np.transpose(lst)[1])
#    return countList

def prob(days,ast,nvc,runs=10):
    countList=[tally(tally(randomBlocks(days,ast,nvc))) for i in range(runs)]
    probList=[np.mean(x) for x in itertools.zip_longest(*countList,fillvalue=0)]
    stdList=[np.std(x) for x in itertools.zip_longest(*countList,fillvalue=0)]
    #probList/=(np.sum(probList)/100.)
    probList/=((np.ceil(days*24/ast)+1)/100.)
    stdList/=((np.ceil(days*24/ast)+1)/100.)
    return np.transpose([probList,stdList])

# p=prob(days,averageServiceTime,numberOfVesselCalls,numberOfTrials)
def drawGraph(days,averageServiceTime,numberOfVesselCalls,numberOfTrials):
    p=prob(days,averageServiceTime,numberOfVesselCalls,numberOfTrials)
    fig, ax = plt.subplots()
    ax.errorbar(range(1,len(p)),p[1:,0],yerr=p[1:,1])
    ax.set_xlabel("$N_v$")
    ax.set_ylabel("$\mathcal{P}(N_v)$")
    ax.set_title("Percentage probability of $N_v$ overlapping vessel calls")
    fig.set_size_inches(w=15,h=8)
    plt.show()

def callDrawGraph():
    if daysInput.get().strip()=="" or averageServiceTimeInput.get().strip()=="" or numberOfVesselCallsInput.get().strip()=="" or numberOfTrialsInput.get().strip()=="":
        messagebox.showwarning("Please fill all fields")
    else:
        getDays = int(daysInput.get())
        getAverageServiceTime = int(averageServiceTimeInput.get())
        getNumberOfVesselCalls = int(numberOfVesselCallsInput.get())
        getNumberOfTrialsInput = int(numberOfTrialsInput.get())
        drawGraph(getDays,getAverageServiceTime,getNumberOfVesselCalls,getNumberOfTrialsInput)


root = Tk()
root.title("Vessel Probability")

frame = LabelFrame(root, text="Statistics", padx=50, pady=50)
frame.pack()

inputFrame = LabelFrame(frame)
inputFrame.pack()

buttonFrame = LabelFrame(frame)
buttonFrame.pack()

getChart = Button(buttonFrame, text="Get Chart", command=callDrawGraph)
getChart.pack(pady=10)

daysLabel = Label(inputFrame, text="Days")
daysLabel.grid(row=0, column=0)

daysInput = Entry(inputFrame)
daysInput.grid(row=0, column=1)

averageServiceTimeLabel = Label(inputFrame, text="Average Service Time")
averageServiceTimeLabel.grid(row=1, column=0)

averageServiceTimeInput = Entry(inputFrame)
averageServiceTimeInput.grid(row=1, column=1)

numberOfVesselCallsLabel = Label(inputFrame, text="Number of Vessel Calls")
numberOfVesselCallsLabel.grid(row=2, column=0)

numberOfVesselCallsInput = Entry(inputFrame)
numberOfVesselCallsInput.grid(row=2, column=1)

numberOfTrialsLabel = Label(inputFrame, text="Number of Trials")
numberOfTrialsLabel.grid(row=3, column=0)

numberOfTrialsInput = Entry(inputFrame)
numberOfTrialsInput.grid(row=3, column=1)

root.mainloop()