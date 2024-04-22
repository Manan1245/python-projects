def add(a,b):        
    return round(a+b) 
r=add(3.2,4.79)      
print(r)  

n=10        
def inc():   
    global n
    print(n)
    n+=1     
    return n 
val=inc()    
print(val)   
print(n) 
