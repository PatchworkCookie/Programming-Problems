'''
Programming problems from the following blog-post:
https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

Problem 3
Write a function that computes the list of the first 100 Fibonacci numbers. By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two. As an example, here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.
'''

def fibonacciSequence(length):
	a, b = 0, 1
	sequence = []
	for i in range(length):
		sequence.append(a)
		c = b
		b = a + b
		a = c # What b used to be
	return sequence
	
if __name__ == '__main__':
	print("Here are the first 100 Fibonacci numbers:")
	print(fibonacciSequence(100))