# Y
s=open("data.txt").readline()
k=0
c=""
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    temp=s.count("E"+i)
    if temp>k:
        k=temp
        c=i
print(c)