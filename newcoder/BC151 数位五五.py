#描述
#求出[a,b]区间内有多少个数数位之和为5的倍数
#输入描述：
#输入一行包含两个整数a,b (1<= a<= b<=1000000)

# 举例14和19的数位和为5和10，符合条件 

## 注意区间里面的数不一定是2位数哦
a, b = input().split(" ")
a, b = eval(a), eval(b)
count =0
for item in range(a, b+1):
    item = str(item)
    total =0
    for i in range(len(item)):
        total+=int(item[i])
    if total % 5 == 0:
        count = count + 1

print(count)