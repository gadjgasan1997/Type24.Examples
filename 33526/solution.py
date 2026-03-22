# D
s=open("data.txt").readline()
c=0
results={}
for i in range(len(s)-2):
    current=s[i]
    next=s[i+2]
    if current==next:
        m=s[i+1]
        if m in results:
            results[m]+=1
        else:
            results[m]=1
r=max(results,key=results.get)
print(r)