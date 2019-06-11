a=input()
a=input().split()
a=[int(d) for d in a]
a.sort(reverse=1)
for i in a:
	print(i,end="")
