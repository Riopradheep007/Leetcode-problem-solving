"""
Remove the last value from the list add to the front countinue the cycle again and again.
"""

def Monkey_dance(ls,target,count=1):

    First_value=ls[0]
    new_list=ls[1:]+[First_value]
    print(new_list)
    if target==new_list:
        return count
        
    count+=1
    
    return Monkey_dance(new_list,target,count)
   
ls=[3,6,5,4,1,2]
target=ls
print(Monkey_dance(ls,target))
