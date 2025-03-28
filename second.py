def func(a):
    print(a+2)

func(33)

def second_func(*args):
    a = list(map(str,args))
    print(a)
second_func(2,3,6,8)