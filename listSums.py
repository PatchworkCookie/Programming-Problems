'''
Programming problems from the following blog-post:
https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

Problem 1
Write three functions that compute the sum of the numbers in a given list using a for-loop, a while-loop, and recursion.
'''

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def sumViaFor(numList):
	logging.debug('Start of sumViaFor(%s)' % (str(numList)))
	sum = 0
	for num in numList:
		sum += num
	return sum
	
def sumViaWhile(numList):
	logging.debug('Start of sumViaWhile(%s)' % (str(numList)))
	sum = 0
	while len(numList) != 0:
		sum += numList.pop()
	return sum
	
def sumViaRecursion(numList):
	logging.debug('Start of sumViaFor(%s)' % (str(numList)))
	sum = numList.pop()
	if len(numList) != 0:
		sum += sumViaRecursion(numList)
	return sum