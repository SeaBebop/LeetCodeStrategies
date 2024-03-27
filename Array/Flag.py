def flagChecker(self,arr):
	#The flag checker idea is best used for range questions
	#The creation of arrays are o(1) space. Excellent for limited space questions
	#Any case where the values and elements are linked flag method can be use
	flagger = [False] * len(arr)

	for i in range(len(arr)):
		value = arr[i]
		flagger[value] = True # Now check if that value exist afterwards or if dups, etc
	