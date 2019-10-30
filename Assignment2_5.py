def prime(num):
	for i in range(2,num):
		if(num%i==0):
			print("It is prime number")
			break
		else:
			print("It is not a prime number")
			break

def main():
	num=int(input())
	prime(num)	

if (__name__=="__main__"):
	main()
