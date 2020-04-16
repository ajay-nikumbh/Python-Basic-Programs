#Python program to take marks of 5 subjects and display its marks

m1=int(input("Enter the subject 1 marks "))
m2=int(input("Enter the subject 2 marks "))
m3=int(input("Enter the subject 3 marks "))
m4=int(input("Enter the subject 4 marks "))
m5=int(input("Enter the subject 5 marks "))

avg=(m1+m2+m3+m4+m5)/5

if avg>=90:
	print("Congratz highest grade A")

if avg>=80 and avg<90:
	print("Congratz highest grade B")

if avg>=70 and avg<80:
	print("Congratz highest grade D")

if avg>=60 and avg<70:
	print("Congratz highest grade D")

else :
	print("Unfortunately lowset grade to bad!! Need improvement")