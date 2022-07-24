'''
问题：KiKi今年5岁了，已经能够认识100以内的非负整数，并且并且能够进行 100 以内的非负整数的加法计算。
不过，BoBo老师发现KiKi在进行大于等于100的正整数的计算时，规则如下：

1.只保留该数的最后两位，例如：对KiKi来说1234等价于34；

2.如果计算结果大于等于 100， 那么KIKI也仅保留计算结果的最后两位，如果此两位中十位为0，则只保留个位。

例如：45+80 = 25

要求给定非负整数 a和 b，模拟KiKi的运算规则计算出 a+b 的值。
'''

# 输入描述
# 一行，输入两个非负整数a和b，用一个空格分隔
a, b = input().split(" ")
a, b = int(a), int(b)
if a+b < 100:
    print(a+b)
else:
    c = str(a+b)
    if c[-2] != "0":
        print(c[-2]+c[-1])
    else:
        print(c[-1])