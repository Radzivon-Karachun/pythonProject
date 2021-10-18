# ----------------------------------------
# Program by K.R.S
#
#
# Version       Date        Info
# 1.0.0      2021-10-18     Tutorial
#
# ----------------------------------------

def hello(x):
    if x == 0:
        return
    else:
        print(x, 'Hello world!')
        hello(x - 1)


hello(10)


def summ(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x + summ(x - 1)


z = summ(10)
print(z)


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(1))
