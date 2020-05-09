# Python code to count the number of occurrences 
def countX(lst, x): 
    count = 0
    for ele in lst: 
        if (ele == x): 
            count = count + 1
    return count 
  
# Driver Code 
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8] 
no=int(input("Enter the no which you want to find:"))
print('{} has occurred {} times'.format(no, countX(lst, no)))