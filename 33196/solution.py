# G
s=open("data.txt").readline()
k=0
result=""
for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    temp=s.count("A"+c)
    if temp>k:
        k=temp
        result=c
print(result)