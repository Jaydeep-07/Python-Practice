# Python code to demonstrate 
# checking of element existence 
# using loops and in 
  
# Initializing list  
test_list = [ 1, 6, 3, 5, 3, 4 ] 

no=int(input("Enter the num:"))
# using loop 
for i in test_list: 
    if(i == no) : 
        print ("Element Exists") 
  
  
# using in 
if (no in test_list): 
    print ("Element Exists") 
else:
    print("no not exists")