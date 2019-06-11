a=input()
a=input().split()
f=0
for i in a:
	if(a.count(i)>1):
		f=1
		print(i)
		break
if(f==0):
	print("unique");
