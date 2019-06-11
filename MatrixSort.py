a=input().split()
r=int(a[0])
c=int(a[1])
m=list()
for i in range(r):
	a=input().split()
	a=[int(d) for d in a]
	a.sort()
	m.append(a)
l=list()
for i in range(r-1):
	for j in range(i+1,r):
		if(m[i][0]>m[j][0]):
			t=m[i]
			m[i]=m[j]
			m[j]=t
for i in range(r):
	for j in m[i]:
		print(j,end=' ')
	print("")
