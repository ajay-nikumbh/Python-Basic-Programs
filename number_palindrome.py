# Python program to check if a number a palindrome
rev=0

n=int(input("Enter the value number: "))
temp=n


while n>0:
	
	dig=n%10
	rev=rev*10+dig
	n=n//10
	
if temp==rev:
	print("The number is palindrome ")

else:
	print("The number is not a palindrome")

	