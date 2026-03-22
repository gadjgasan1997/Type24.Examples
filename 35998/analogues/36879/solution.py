# 1001
s=open("data.txt").readlines()
m=0
for i in s:
    if i.count("G")<25:
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if c in i:
                first=i.index(c)
                last=i.rindex(c)
                a=last-first
                m=max(m,a)
print(m)