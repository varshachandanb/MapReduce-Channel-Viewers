import sys

def mapperFunc():
    inputFile1="input1.txt"
    readPtr1=open(inputFile1,"r")
    for line in readPtr1:
        line=line.strip()
        show=line.split(",")[0]
        viewers=int(line.split(",")[1])
        if show not in showList:
            showList[show]=0
        else:
            showList[show]+=viewers
    readPtr1.close()
    inputFile2="input2.txt"
    readPtr2=open(inputFile2,"r")
    for line in readPtr2:
        line=line.strip()
        show=line.split(",")[0]
        channel=line.split(",")[1]
        if channel not in channelList:
            channelList[channel]=[]
        else:
            channelList[channel].append(show)
    readPtr2.close()

def intermediateFunc():
    channels=channelList.keys()
    for c in channels:
        channelViewers[c]=[]
        totalViewers[c]=0
    for ch in channelList:
        for sh in channelList[ch]:
            channelViewers[ch].append(showList[sh])
    print "Intermediate Function:"
    for chan in channelViewers:
        print "Channel: "+chan+'\n'+"Viewers:"+str(channelViewers[chan])+ '\n'



def reducerFunc():
    for i in channelViewers:
        for j in range(len(channelViewers[i])):
            totalViewers[i]+=channelViewers[i][j]
    print "Final Output:"
    for c in totalViewers:
        print "Channel Name: "+c+" Viewers:"+str(totalViewers[c])






if __name__== "__main__":
    #inputFile=sys.argv[1]
    showList={}
    channelList={}
    channelViewers={}
    totalViewers={}
    mapperFunc()
    intermediateFunc()
    reducerFunc()











