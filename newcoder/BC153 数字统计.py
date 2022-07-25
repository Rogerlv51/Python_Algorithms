# 请统计某个给定范围[L, R]的所有整数中，数字2出现的次数。
# 比如给定范围[2, 22]，数字2在数2中出现了1次，在数12中出现1次，在数20中出现1次，
# 在数21中出现1次，在数22中出现2次，所以数字2在该范围内一共出现了6次。


L, R = input().split(" ")
out = 0
for item in list(range(int(L), int(R)+1)):
    #for i in str(item):
    #    if i == "2":
    #        out+=1
    # 可以直接用字符串自带的count函数更加方便
    item = str(item)
    out+=item.count("2")
print(out)