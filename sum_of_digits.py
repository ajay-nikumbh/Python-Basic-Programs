# Program to count the number of digits in a number

n=int(input("Enter the number : "))
count=0
while n>0:
	count+=1
	n=n//10

print("The number of the digits in a number are :",count)