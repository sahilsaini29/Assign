#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sum of First n Natural numbers , Ask user for Number.


def myreduce(num):
    ''' This functionm will return sum of n Natural numbers'''
    num_list=list(range(1,number+1))
    sum_of_elements=0
    
    for i in num_list:
        sum_of_elements+=i
        
    return num_list,sum_of_elements

#Input 
print("Input:")
number=int(input("Please insert the number :"))

#Function Execution

output_value=myreduce(number)

#Output
print("Output:")
print("List of First n Natural numbers are:",output_value[0])
print("Sum of List elements are :",output_value[1])


# In[ ]:




