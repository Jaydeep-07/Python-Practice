# Python3 program to find sum in Nth group 
  
# Check if given array is Monotonic 
def isMonotonic(A): 
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 
  
# Driver program 
A = [6, 5, 4, 4] 
  
# Print required result 
print(isMonotonic(A)) 


#Input : 6 5 4 4
#Output : true

#Input : 5 15 20 10
#Output : false