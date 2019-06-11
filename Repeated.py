n=int(input())
a=input().split()
a=[int(i) for i in a]
#print(a)
b=list()
for i in a:
    if(a.count(i)>1):
        b.append(int(i))
b = list(dict.fromkeys(b))
b.sort()
if(len(b)<=0):
    print("unique")
else:
    for i in b:
        print(i,end=" ")
