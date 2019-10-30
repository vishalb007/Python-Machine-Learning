def main():
	num=int(input())
	count=0
	while num>0:
		num=num//10
		count=count+1
	print(count)
	
if (__name__=="__main__"):
	main()
