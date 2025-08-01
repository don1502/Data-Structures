a= int(input())
b=[]
count = 0
for i in range (1,a+1):
    if a%i==0:
        b.append(i)
for i in b:
    if i%2==1:
        count+=1
print(count)