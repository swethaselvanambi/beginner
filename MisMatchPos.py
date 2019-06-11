a=int(input())
a=input().split()
a=[int(d) for d in a]
for i in range(len(a)):
	if(((a[i]%2==0)&(i%2!=0))|((a[i]%2!=0)&(i%2==0))):
		print(a[i],end=" ")
