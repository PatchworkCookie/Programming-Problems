'''
Programming problems from the following blog-post:
https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

Problem 4
Write a function that given a list of non negative integers, arranges them such that they form the largest possible number. For example, given [50, 2, 1, 9], the largest formed number is 95021.

9000
3
211
21121
21111
124
121
12111
1200
1
'''

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#Sort numbers by most significant digits
def sortBySignificance(listOfNums):
	logging.debug('Starting sortBySignificance(%s)' % (str(listOfNums)))
	sorted = []
	for num in listOfNums:
		if num < 0:
			raise ValueError("Value '%s' must be non-negative" % (str(num)))
		#Check if num should be ahead of the current sorted num
		#TODO: This loop is fucked
		'''
		for sortedNum in sorted:
			logging.debug("Checking num '%s' against sortedNum '%s'" % (str(num), str(sortedNum)))
			logging.debug("Sorted: %s" % (str(sorted)))
			#Check if next most significant digit is higher
			i = 0
			for digit in str(num):
				logging.debug("Digit: %s sDigit: %s" % (str(digit), str(sortedNum)[i]))
				if int(digit) > int(str(sortedNum)[i]):
					sorted.insert(sorted.index(sortedNum),num) #Insert num ahead of the current sortedNum
					i += 1
				#else: continue
				'''
		#Insert num into the sorted list
		sorted.insert(0,num)
		logging.debug("Sorted list is now: %s" % (str(sorted)))
		'''
		'''
		pass
	pass

def testBiggerSum(num1, num2):
	logging.debug('Start of testBiggerSum(%s, %s)' % (str(num1), str(num2)))
	sum1 = int(str(num1) + str(num2)) # Concatenate the numbers and convert to int
	sum2 = int(str(num2) + str(num1))
	logging.debug('sum1: %s, sum2: %s' % (str(sum1), str(sum2)))
	if sum1 < sum2: 
		logging.debug('sum1: %s < sum2: %s' % (str(sum1), str(sum2)))
		return -1
	if sum1 > sum2: 
		logging.debug('sum1: %s > sum2: %s' % (str(sum1), str(sum2)))
		return 1
	if sum1 == sum2: 
		logging.debug('sum1: %s = sum2: %s' % (str(sum1), str(sum2)))
		return 0
	
	
	pass
#Convert numbers to strings
#Concatenate strings
#Return numbers

if __name__ == '__main__':
	sortBySignificance([1,2])