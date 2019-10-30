def check(num1):
	if num1 > 0:
		print ("Positive Number")
	elif num1 < 0:
		print ("Negative Number")	
	else :
		print ("Zero")	

def main():
	num1=int(input())
	check(num1)

if (__name__=="__main__"):
	main()

