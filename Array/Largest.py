# Python3 program to find maximum 

# Python 3 code to find sum  
# of elements in given array 
def FindLargets(arr,n):

    max=arr[0]
    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
    return max

def main():

    arr=[12,17,3,4,5]

    n=len(arr)

    ans=FindLargets(arr,n)

    print("Largest:",ans)
if __name__=="__main__":
    main()