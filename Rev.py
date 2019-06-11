a=input()
a=input().split()
a=[int(d) for d in a]
a.sort(reverse=1)
n=0
for i in a:
	n=n*10+i
print(n)
