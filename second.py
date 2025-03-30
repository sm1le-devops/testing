def func(a):
    return a+23



def second_func(*args):
    a = list(map(str,args))
    return a

def second_1(c):
    return c

a = second_func(2,3,6,8)
a.append(str(func(33)))
print(a*second_1(2))