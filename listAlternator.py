'''
Programming problems from the following blog-post:
https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

Problem 2
Write a function that combines two lists by alternatingly taking elements. For example: given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].
'''

import logging

def alternateLists(firstList, secondList):
	newList = []
	
	if len(firstList) >= len(secondList):
		length = len(firstList)
	else: length = len(secondList)
	
	for i in range(length):
		if len(firstList) > i:
			newList.append(firstList[i])
		if len(secondList) > i:
			newList.append(secondList[i])
			
	return newList