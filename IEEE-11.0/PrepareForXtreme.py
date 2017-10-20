
time = []
topics = []
originTopic =[]
allTopics =[]
minTime = 0

inp1 = raw_input()


while True:
    inp = inp1.strip().split(' ')
    time.append(int(inp.pop(0)))
    topics.append(inp)
    originTopic.append(inp)
    
    inp1 = raw_input()
    print(inp1=='')
    
    
    if not inp1:
        break
    


def allTopicsFunc(topics , allTopics):
	topics.sort(key=len, reverse=True)
	allTopics=topics[0]
	for i in range(1,len(topics)):
		if (len(list(set(topics[i]) - set(allTopics))) > 0):
			item = list(set(topics[i]) - set(allTopics))
			allTopics = allTopics + item
	return allTopics

def calculateTime (topics ,time, allTopics ,minTime):
	topics.sort(key=len, reverse=True)
	for i in range(len(topics)):
		if (set(topics[i]) == set(allTopics)):
			minTime = time[i]

		elif((i != len(topics)-1) and len(list(set(topics[i])) + list(set(topics[i+1]))) >= len(allTopics)):
			indx = originTopic.index(topics[i])
			temp = time[indx-1] + time[indx]
			if(minTime > temp ):
				minTime =temp

	return minTime

allTopics = allTopicsFunc(topics , allTopics)
result = calculateTime (topics ,time, allTopics ,minTime)
print (result)



	

