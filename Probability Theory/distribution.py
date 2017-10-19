import numpy as np

def factorial(x):
    if x > 1:
        return factorial(x-1) * x
    else:
        return 1

# poisson distribution
def poisson(lambda_num,k):
    k_factorial = factorial(k)
    molecular = pow(lambda_num,k)
    
    return (float(molecular) / k_factorial) * np.exp(-lambda_num)

#C(n,m) = n!/(m!*(n-m)!) 
def combinations(n,m):
    a = factorial(n)
    b = (factorial(m) * factorial(n-m))
    return  a / b 


def bernoulli(k,n,p):
    a = combinations(k,n)
    b = pow(p,2)
    c = pow(1 - p,k - n)
    
    return  a * b * c

print poisson(lambda_num = 2 ,k = 5)
print bernoulli(k = 4 ,n = 2 ,p = float(1)/3)


    
