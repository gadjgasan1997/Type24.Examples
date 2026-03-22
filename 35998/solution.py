# 1004
s=open("data.txt").readlines()
m=0
for i in s:
    if i.count("A") < 25:
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if c in i:
                first= i.index(c)
                last= i.rindex(c)
                d= last - first
                m=max(m,d)
print(m)