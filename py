#0 , 1 le terme que je vais écrire est la somme des 2 derniers termes 
# f(0) = 0 
# f(1) = 1
# f(2) = f1+f0
# f(3) = f2 + f1
# f(n) = f(n-1) + f(n-2)

#écrire une fonction qui prend un argument n et qui retourne fn 
from functools import cache
@cache
def fibonacci(n):
    if n == 0 :
        return 0
    
    if n == 1 : 
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))
