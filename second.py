def func(a):
    return a+23



def second_func(*args):
    a = list(map(str,args))
    return a


a = second_func(2,3,6,8)
a.append(func(33))
print(a)