# 问题描述
# 对一个素数的回文数判断其是不是也是素数，是则输出prime，不是则输出noprime
# 例如13的回文数131是素数，而17的回文数171则不是素数

# 第一次尝试：运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# 下面算法复杂度过高
import math
x = input()
x = x + x[-2::-1]
numx = eval(x)
tag = True

## 这题的一个小trick是要注意复杂度问题，因此这里对总体数组开根号，不影响整体信息
for item in range(2, int(math.sqrt(numx))):
    if numx%item == 0:
        tag = False
        break
if tag:
    print("prime")
else:
    print("noprime")