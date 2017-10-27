#实现阶乘

#1! = 1*1
#2! = 1*2
#3! = 1*2*3
#4! = 1*2*3*4
#5! = 1*2*3*4*5


#1 + 2 + 3 +4 + 5
def f(n):
    param = 1
    for i in range(1,n+1):
        param *= i
    return param

print(f(6))

# sum = 1
# for i in range(1,6):
#     sum *= i
#     #print(sum)
# print(sum)

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(5))

#递归的特点:1:调用自身函数 2有结束条件
#但凡是递归可以写的循环都可以解决
#递归在很多时候效率低下


#斐波那契
# 0 1 1 2 3 5 8 13 21 43

#feibo(1) = 0
#feibo(1) = 2

#从1开始
def feibo(n):
    #if n == 1 or n == 2:
    if n <= 1:
        return 1
    return feibo(n - 1) + feibo(n - 2)

 # n 默认从0开始走 if n <= 1 return n
#从0开始
def fibo_new(n):  # n可以为零，数列有［0］

    if n <= 1:
        return n
    return (fibo_new(n - 1) + fibo_new(n - 2))

print(feibo(3)) #从1开始
print(fibo_new(3)) #从0开始



#feibo(2) = fei(0) + feibo(1)





