a=input()
a=[int(d) for d in a]
while(a[len(a)-1]==0):
	a.pop()
i=0
f=0
j=len(a)-1
while(i<j):
	if(a[i]!=a[j]):
		print("no")
		f=1;
	i+=1
	j+=1
if(f==0):
	print("yes")
