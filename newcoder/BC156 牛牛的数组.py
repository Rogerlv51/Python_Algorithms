# 描述
# 牛牛刚学会数组不久，他拿到两个数组 a 和 b，询问 b 的哪一段连续子数组之和与数组 a 之和最接近。
# 如果有多个子数组之和同样接近，输出起始点最靠左的数组。

# 输入描述：
# 第一行输入两个正整数 n 和 m ，表示数组 a 和 b 的长度。
# 第二第三行输入 n 个和 m 个正整数，表示数组中 a 和 b 的值。

# 输出子数组之和最接近 a 的子数组
## 这个题还是值得一做的，中等难度（mmp第一次写还是花了好长时间，另外感觉写的好像复杂了点，输出那里）

n, m = list(map(int, input().split(" ")))
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))
sum_a = sum(a)
minest = abs(b[0]-sum_a)
minlist = b[0]
for i in range(m):
    for j in range(i+1, m+1):
        if (abs(sum(b[i:j])-sum_a)) < minest:
            minest = abs(sum(b[i:j])-sum_a)
            minlist = b[i:j]
print(str(minlist).replace(",","").strip("[").strip("]"))
