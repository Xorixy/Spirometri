# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 16:41:16 2017

@author: Neo
"""

# -*- coding: utf-8 -*-
#384, 512, 3
#Linn (Snurr3) 1 187 skip
#Linn (Snurr6) 243
"""
Created on Mon Jun 26 13:36:31 2017

@author: Neo
"""
skip = 0
import numpy as np
import cv2
import matplotlib.pyplot as plt
#from scipy import stats


def printaFlera(manylists):
    for p in range (len(manylists)):
        for q in range (len(manylists[p]) - 1):
            manylists[p][q] *= 2.5
        xaxel = []
        for q in range(len(manylists[p])):
            xaxel.append(q/5)
        plt.scatter(xaxel, manylists[p]);
        plt.plot(xaxel, manylists[p]);
    plt.suptitle('', fontsize=20)
    plt.xlabel('Time(s)', fontsize=18)
    plt.ylabel('Rotations/s', fontsize=16)
    plt.savefig('Philip.svg')
    plt.show

def plotta(x, y):   
    plt.scatter(x,y)
    plt.plot(x, y)
    plt.show()
    

def countPixlar(color_array, cap, frames, skip):
    for p in range (frames-1):
        #Läser in en bild
        ret, frame = cap.read()
        #Skippar upp till skip-värdet
        if(p < skip):
            continue
        snurr = frame
        #Avgrämsar till den relevanta delen
        snurr = frame[92:641, 247:997]
        #snurr = frame[76:598, 233:662]
        #Omvandlar bilden till gråskala
        gray = cv2.cvtColor(snurr, cv2.COLOR_BGR2GRAY)
        #Tar medelvärdet av alla pixlarna
        average_color_per_row = np.average(gray, axis=0)
        average_color = np.average(average_color_per_row, axis=0)
        color_array[p - skip] = average_color
    return color_array;

def frequency(freqlist, color_array, medel):
    c = 0 #räknare, räknar upptill 24 
    k = 0 #räknare, räknar antalet extrempunkter/vändningar
    p = 0  #räknare som loopar genom listan
    while p < len(color_array) :
        if color_array[p] > medel:
            while p < len(color_array) and color_array[p]> medel:
                if c == 47:
                    c = 0
                    freqlist.append(k)
                    k = 0 
                
                p = p+1
                c= c+1 
            k += 1
    
        else:
            while p < len(color_array) and color_array[p] <= medel: 
                if c == 47:
                    c = 0
                    freqlist.append(k)
                    k = 0 
                
                p = p+1
                c = c+1
            k = k +1 
    return freqlist;

def getFreqList(name, skip):
    cap = cv2.VideoCapture(name)

    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    color_array = np.zeros(frames - skip)
    medel = 0


    #Skapar en lista med medelvärdena av pixlarnas ljusintensitet per bild
    
    color_array = countPixlar(color_array, cap, frames, skip)
    
    #Medelvärdet av pixlarna genom hela filmen

    medel = np.mean(color_array)
    
    freqlist = []

    freqlist = frequency(freqlist, color_array, medel)
    return freqlist
    
def printaLista(freqlist):
    for q in range (len(freqlist) - 1):
        freqlist[q] *= 2.5
    xaxel = []
    for q in range(len(freqlist)):
        xaxel.append(q/5)
    
    plt.scatter(xaxel, freqlist);
    plt.plot(xaxel, freqlist);
    plt.show();    


        

def exportLista(thelist, name):
    thefile = open(name, 'w')
    for item in thelist:
        thefile.write("%s\n" % item)

def readLista(name):
    thefile = open(name, 'r')
    lines = thefile.read().split('\n')
    lines2 = []
    for i in range(len(lines) - 1):
        lines2.append(lines[i])
    lines2 = list(map(float, lines2))
    return lines2



def getMax(freqlist):
    largestValue = 0
    for number in freqlist:
        if number > largestValue:
            largestValue = number;
    return largestValue

def getCArray(name, skip):
    cap = cv2.VideoCapture(name)

    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    color_array = np.zeros(frames - skip)


    #Skapar en lista med medelvärdena av pixlarnas ljusintensitet per bild
    
    color_array = countPixlar(color_array, cap, frames, skip)
    #Medelvärdet av pixlarna genom hela filmen
    return color_array
#def printMaxes()


#Hur många bilder som ska skippas i början
skip = 0
#lista = getFreqList(name, skip)

flerlist = []



names = ['Philip']
namnum = [5]




printaFlera(flerlist)
"""
for p in range(len(names)):
    for q in range(namnum[p]):
        namtxt = "z"
        name = names[p]
        name += ' ('
        name += str(q+1)
        name += ').'
        namov = name
        namtxt += name
        namov += 'MOV'
        namtxt += 'txt'
        printaLista(readLista(namtxt))

maxlist = []

for p in range(len(names)):
    templist = []
    for q in range(namnum[p]):
        namtxt = "z"
        name = names[p]
        name += ' ('
        name += str(q+1)
        name += ').'
        namtxt += name
        namtxt += 'txt'
        templist.append(readLista(namtxt))
    for q in range(len(templist)):
        templist[q] = getMax(templist[q])
    maxlist.append(getMax(templist)*2.5)
peflist = [660, 620, 420, 615, 420, 570, 410, 420, 660]

plotta()
"""


