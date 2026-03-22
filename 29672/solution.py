# 467
s=open("data.txt")
k=0
for line in s:
    a=line.count("A")
    e=line.count("E")
    if a<e:
        k+=1
print(k)