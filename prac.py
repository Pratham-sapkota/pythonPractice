name="123"


try:          #first the compiler runs the "try" structure.
    number=int(name)
    
except:       #if there is somthing wrong in the code , except structure is executed
    number=-1
 
print("First",number)