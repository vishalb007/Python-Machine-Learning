def main():
	num =int(input())
	for i in range(2,num+2):
		for j in range(1,i):
			print(j,end=" ")
		print()

if (__name__=="__main__"):
	main()
