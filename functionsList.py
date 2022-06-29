# f(x) = x + 2

# domain = [1,2,3,4,5,6]
# f(x) = x + 2
# domain(input):range(output)
# 1 ----------> 3
# 2 ----------> 4
# 3 ----------> 5
# 4 ----------> 6
# 5 ----------> 7
# 6 ----------> 8


# domain container
domain_values = []

n = 6

#populating the domain container
#with values from 1 to 6 
for i in range(1,n+1):
    domain_values.append(i)

print(domain_values)


#f(x) = x + 2

def f(x):
    return x + 2 

def range_values():
     res = []

     for i in domain_values:
         res.append(f(i)) 
     return res 


range_values = range_values()

print('f(x) = x + 2')


for x,y in zip(domain_values,range_values):
    print(" {} -------> {} ".format(x,y))




#dictioneries, tuples



     




