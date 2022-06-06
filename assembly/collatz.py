def collatz (n, initialValue):
	i = 1	
	while (True):
		if (i == n):
			return initialValue
		elif (initialValue == 1):
			return 0
		elif(initialValue % 2 == 0):
			initialValue = initialValue/2
			i = i + 1
		else:
			initialValue = initialValue * 3
			initialValue = initialValue + 1
			i = i + 1
	

print(collatz(5, 11))
print(collatz(20, 11))