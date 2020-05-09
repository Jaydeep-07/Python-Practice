# Python3 program to find compound 
# interest for given values. 

def compound_interest(principle, rate, time): 

	# Calculates compound interest 
	CI = principle * (pow((1 + rate / 100), time)) 
	print("Compound interest is", CI) 

# Driver Code 
def main():
    principle=float(input("Enter the principle amt:"))
    rate=float(input("Enter the rate:"))
    time=float(input("Enter the time:"))
    
    compound_interest(principle,rate,time) 
if __name__=="__main__":
    main()

