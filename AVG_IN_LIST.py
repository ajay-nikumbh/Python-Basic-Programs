n=int(input("Enter the number of the elements to be inserted: "))
a=[]
for i in range(0,n):
	element=int(input("Enter the elements: \n"))
	a.append(element)
avg=sum(a)/n
print("The average of elements in the list: \n",round(avg,3))