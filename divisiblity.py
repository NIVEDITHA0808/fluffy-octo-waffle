def digits(m,n,x,count):
    
     p = int(m)
     q = int(n)
     r = int(x)
     
     while p<=q :
         if p%r == 0:
             count += 1
             
         p += 1
      
     return(count)

count = 0        
a = input("No. of digits: ")
x = input("divisibility rule of ")

print("No. of "+a+" digit numbers divisible by "+x)

m = input("from ")
n = input("to ")

print("is:")
print(digits(m,n,x,count))
 
