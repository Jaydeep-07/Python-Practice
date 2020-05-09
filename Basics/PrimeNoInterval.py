
def IsPrime(start,end):

    for val in range(start,end+1):
        if val>1:
            for n in range(2,val):
                if(val%2)==0:
                    break
            else:
                print(val)

def main():
    start=int(input("Enter the start no:"))
    end=int(input("Enter the rend no:"))
    
    IsPrime(start,end)
if __name__=="__main__":
    main()