n=int(input())
c=0
b=list()
for i in range(n):
	s=0
	a=[int(d) for d in str(i)]
	for j in a:
		s+=j
	if(i+s==n):
		b.append(i)
		c+=1
print(c)
if(len(b)):
	for i in b:
		print(i)
