def Fact(n):
    fact=1
    for i in range(1,n+1):
        fact=i*fact
    return fact

def main():
    n=int(input("Enter the no"))
    f=Fact(n)
    print("Factorial:",f)
if __name__=="__main__":
    main()