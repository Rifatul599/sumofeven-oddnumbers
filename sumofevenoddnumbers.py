num = int(input("enter a number :"))
even=odd=0
x=1
while x<=num :
    if x%2==0:
        even+=x
    else:
        odd+=x
    x+=1

print("sum of even number is",even)
print("sum of odd number is",odd)







