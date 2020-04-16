# python program to read a number and compute n+nn+nnn

n=int(input("Enter the value number n: "))
temp=str(n)
t1=temp+temp
t2=temp+temp+temp
print(t1,"------",t2)
result=n+int(t1)+int(t2)
print(result)