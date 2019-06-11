a=input().split()
for j in a:
	b=[ i for i in j]
        for i in range(len(b)-1,-1,-1):
		print(b[i],end="")
	print(" ")
