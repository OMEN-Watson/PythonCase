# E1: n^2
def func_a(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total = total + i * j
    return total
# n^2


def fun_b(n):
    total = 0
    for i in range(100 * n):
        for j in range(10):
            # 3 operations , 30 operations totally
            total = total + i * j 
    return total
# 3*100*n, O(n)

def fun_c(n):
    total = 0
    for i in range(100):
        for j in range(n):
            # 3 operations, 3n operations totally
            total = total + i * j
        for k in range(n):
            # same as the above
            total = total + i * k
        for l in range(100):
            # 300 operations
            total = total + i * l
    return l
# (3n+3n+300)*100, O(n)

strTest='abcde12345'
print(strTest[0:20])