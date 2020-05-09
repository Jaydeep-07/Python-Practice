# Python 3 code to find sum  
# of elements in given array 
def FindSum(arr,n):

    return (sum(arr))

def main():

    arr=[12,2,3,4,5]

    n=len(arr)

    ans=FindSum(arr,n)

    print("Sum:",ans)
if __name__=="__main__":
    main()