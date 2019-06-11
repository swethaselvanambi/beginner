n=int(input())
a=list()
for i in range(0,n):
    b=input()
    a.append(b)
a=input()
a=[int(i) for i in a]
#print(a)
b=list()
for i in a:
    if(a.count(i)>1):
        b.append(int(i))
b = list(dict.fromkeys(b))
b.sort()
for i in b:
    print(i,end=" ")
