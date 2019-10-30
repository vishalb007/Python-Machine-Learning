def main():
	num=int(input())
	sum=0
	while num>0:
		sum=sum+(num%10)
		num=num//10
	print(sum)
	
if (__name__=="__main__"):
	main()
