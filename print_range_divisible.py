# Python program to find the sum of the digits in number
tot=0
n=int(input("Enter the number : "))
while n>0:
	dig=n%10
	tot=tot+dig
	n=n//10
print("Sum of the digits of a number",tot)