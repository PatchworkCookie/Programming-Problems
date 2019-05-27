'''
Programming problems from the following blog-post:
https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

Problem 5
Write a program that outputs all possibilities to put + or - or nothing between the numbers 1, 2, ..., 9 (in this order) such that the result is always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 = 100.
'''
'''
How can I solve this...

Brute-force: Attempt every combination of possibilities, save only those that succeed
	Pros: Probably the simplest way
	Cons: It may require a LOT of calculations/time
	
Strategic: Start from one side of the list of numbers and try to keep the running total as close to 100 as possible
	Pros:
	Cons: This seems like it will be WAY more complicated, 
		Could end up missing stuff if I'm not careful
'''

import itertools
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Go through every combination of +/-/None
# itertools.product('None-+')
def magicSum(listOfNumbers, targetSum):
	listOfSolutions = []
	return listOfSolutions

# Take the list of numbers and stitch it together into either a number or equation
def implementOperators(listOfNumbers, operatorTuple):
	if len(listOfNumbers) != len(operatorTuple)+1:
		raise ValueError('The number of operators must be one less than the number of digits.')
	outputString = ''
	for i in range(len(operatorTuple)):
		outputString += str(listOfNumbers[i])
		if operatorTuple[i] != '_': # Ignore '_', append other symbols
			outputString += operatorTuple[i]
	outputString += str(listOfNumbers[-1])
	return outputString

# find the result of the equation
#eval(string)

# Save the successful combinations

