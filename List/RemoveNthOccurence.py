#  program to remove Nth  
# occurrence of the given word 
  
# Function to remove Ith word 
def RemoveIthWord(list, word, N): 
    count = 0
      
    for i in range(0, len(list)): 
        if (list[i] == word): 
            count = count + 1
              
            if(count == N): 
                del(list[i]) 
                return True
                  
    return False
  
# Driver code 
list = ['Jaydep', 'for', 'patil','Jaydeep'] 
word = 'Jaydeep'
N = 1
  
flag = RemoveIthWord(list, word, N) 
  
if (flag == True): 
    print("Updated list is: ", list) 
else: 
    print("Item not Updated")  