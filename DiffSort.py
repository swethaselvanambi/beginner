n=int(input())
a=list()
for i in range(n):
	b=input().split()
	b=[int(d) for d in b]
	for j in b:
		a.append(j)
a.sort()
for i in a:
	print(i,end=" ")
