# Python program to reverse a given number

n=int(input("Enter the value number to be reversed: "))
while n>0:
	dig=n%10
	rev=rev*10+dig
	n=n//10
print("The reverse of the number : ",rev)