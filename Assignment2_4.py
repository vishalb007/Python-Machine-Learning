def main():
	sum=0
	num =int(input())
	for i in range(1,num+1):
		if num%i==0:
			sum=sum+i
	print(sum)

if (__name__=="__main__"):
	main()
