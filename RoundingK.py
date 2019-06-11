a=input().split()
k=int(a[1])
n=int(a[0])
a=[int(d) for d in a[0]]
f=0
p=1;
while(f==0):
	prod=p*n
	l=[ int(d) for d in str(prod)]
	c=0
	j=len(l)-1
	while(l[j]==0):
		c+=1
		j-=1
	if(c==k):
		print(prod)
		f=1
	p+=1
