def FindSum(n):
    sum=0
    for i in range(1,n+1):

        sum=sum+(i*i)
    print(sum)

def main():
    n=int(input("Enter the no:"))
    FindSum(n)
if __name__=="__main__":
    main()