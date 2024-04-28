#Dealing with dups or missing ranges

from collection import defaultdict

def duplicationChecker(self,arr):
  #The idea is to use dictionaries to maintain count amount of given array
  dupDict = defaultdict(int)
  #As the loop goes through the array, it will increment the fequency of the value being seen
	for x in arr:
		dupDict[x]+=1
		if dupDict[x] > 1:
			return True
  #There are 3 general things you can do:
    #Check for > 1, Checking if there is a dup
    #Check for 0 or "if value in dict", Checking if it doesnt exist in a range
    #Check for < 1, Checking how many extra values are needed to filful specific requests
