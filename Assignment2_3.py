def fact(num):
	if(num==1):
		return num
	else:
		return num*fact(num-1)

def main():
	num =int(input())
	if num==0:
		print("1")
	elif num<0:
		print("wrong input")
	else:		
		print(fact(num))

if (__name__=="__main__"):
	main()
