# 1713
s = open("data.txt").readline()
m = 0
n = s.split("XZZY")

for i in n:
    j = len(i) + 6
    m = max(m, j)

print(m)