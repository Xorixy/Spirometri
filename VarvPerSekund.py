import numpy as np
import cv2
import matplotlib.pyplot as plt
#from scipy import stats

#Takes an array containing frequency lists and makes a graph from each frequency list
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

    
#Analyses a film and returns a list containing the mean light intensity of each frame
def countPixlar(color_array, cap, frames, skip):
    for p in range (frames-1):
        #Reads a frame
        ret, frame = cap.read()
        #Skips to the skip value
        if(p < skip):
            continue
        snurr = frame
        #Cuts the movie into the relevant parts
        snurr = frame[92:641, 247:997]
        #Turns the picture into grayscale
        gray = cv2.cvtColor(snurr, cv2.COLOR_BGR2GRAY)
        #Calculates the mean value of the frame
        average_color_per_row = np.average(gray, axis=0)
        average_color = np.average(average_color_per_row, axis=0)
        color_array[p - skip] = average_color
    return color_array;

#Calculates how many times the light intensity crossed the mean value of the whole film
# for every 48 frames, then returns that in a list
def frequency(freqlist, color_array):
    #Calculates the mean value of the whole film
    medel = np.mean(color_array)
    c = 0 #Counter, counts up to 47
    k = 0 #Counter, counts the total times that the light intensity crossed the mean value
    p = 0 #Counter, loops through the whole film
    while p < len(color_array) :
        #Loops until the light intensity in the frame goes under the mean
        if color_array[p] > medel:
            while p < len(color_array) and color_array[p]> medel:
                if c == 47:
                    c = 0
                    freqlist.append(k)
                    k = 0 
                
                p = p+1
                c= c+1 
            k += 1
        
        #Loops until the light intensity in the frame goes over the mean
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

#Takes a movie and returns a frequency list containing the times the light intensity crossed the mean value per 48 frames
def getFreqList(name, skip):
    #Reads the film
    cap = cv2.VideoCapture(name)
    
    #Counts the number of frames
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    color_array = np.zeros(frames - skip)


    #Creates a list of the mean light intensity values per frame
    
    color_array = countPixlar(color_array, cap, frames, skip)
        
    freqlist = []
    
    #Creates a list of the times the light intensity crossed the mean
    freqlist = frequency(freqlist, color_array)
    return freqlist
    

#Makes a graph from a frequency list
def printaLista(freqlist):
    for q in range (len(freqlist) - 1):
        freqlist[q] *= 2.5
    xaxel = []
    for q in range(len(freqlist)):
        xaxel.append(q/5)
    
    plt.scatter(xaxel, freqlist);
    plt.plot(xaxel, freqlist);
    plt.show();    


        
#Exports a frequency list to a txt
def exportLista(thelist, name):
    thefile = open(name, 'w')
    for item in thelist:
        thefile.write("%s\n" % item)

#Imports a frequency list from a txt
def readLista(name):
    thefile = open(name, 'r')
    lines = thefile.read().split('\n')
    lines2 = []
    for i in range(len(lines) - 1):
        lines2.append(lines[i])
    lines2 = list(map(float, lines2))
    return lines2


#Gets the max value of a list
def getMax(freqlist):
    largestValue = 0
    for number in freqlist:
        if number > largestValue:
            largestValue = number;
    return largestValue

#Gets a list containing the mean light intensity for each frame of a video
def getCArray(name, skip):
    cap = cv2.VideoCapture(name)

    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    color_array = np.zeros(frames - skip)


    #Skapar en lista med medelvärdena av pixlarnas ljusintensitet per bild
    
    color_array = countPixlar(color_array, cap, frames, skip)
    #Medelvärdet av pixlarna genom hela filmen
    return color_array




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


