n= int(input())
k = int(input())
a=[]
sum=0
for i in range (0,n):
    b=int(input())
    a.append(b)
roated = a[-k:]+a[:-k]

for i in range (0,n):
    if i % 2 == 0:
        sum+=roated[i]

print(sum)