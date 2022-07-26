# 这个题还是蛮难的，显示中等难度(其实也不是很难，一开始没理解题意，但是要思考的细节很多，有意思)

# 对于10进制数87：  可以通过n步加法得到一个回文数
# STEP1：87+78  = 165                  STEP2：165+561 = 726
# STEP3：726+627 = 1353                STEP4：1353+3531 = 4884
# 在这里的一步是指进行了一次N进制的加法，上例最少用了4步得到回文数4884。
# 注意这里每一次加法都是加上把本身翻转后的数

# 写一个程序，给定一个N（2<=N<=10或N=16）进制数M（100位之内），求最少经过几步可以得到回文数。
# 如果在30步以内（包含30步）不可能得到回文数，则输出“Impossible!”
# 进制N>10时，使用大写'A'字母表示10，'B'表示11,...,'E'表示16

# 感觉一个首先的思路是，对于输入的不同进制得先统一进制

def to_ten(x, N):     # 任意输入进制转成10进制
    number = 0
    for i in range(len(x)):
        if x[i]=="A":
            number+=10*int(N)**(len(x)-1-i)
        elif x[i]=="B":
            number+=11*int(N)**(len(x)-1-i)
        elif x[i]=="C":
            number+=12*int(N)**(len(x)-1-i)
        elif x[i]=="D":
            number+=13*int(N)**(len(x)-1-i)
        elif x[i]=="E":
            number+=14*int(N)**(len(x)-1-i)
        elif x[i]=="F":
            number+=15*int(N)**(len(x)-1-i)
        else:
            number+=int(x[i])*int(N)**(len(x)-1-i)
    return number

def ten_ToAny(N, x):    # 将10进制转回一开始的输入进制，N为进制
    N= int(N)
    ls = []
    while True:
        div, mod = divmod(x, N)
        ls.append(mod)
        x = div
        if x==0:
            break
 
    temp_list=list(map(str, ls[::-1]))
    for i in range(len(temp_list)):
        if temp_list[i] == '10':
            temp_list[i] = 'A'
        elif temp_list[i] == '11':
            temp_list[i] = 'B'
        elif temp_list[i] == '12':
            temp_list[i] = 'C'
        elif temp_list[i] == '13':
            temp_list[i] = 'D'
        elif temp_list[i] == '14':
            temp_list[i] = 'E'
        elif temp_list[i] == '15':
            temp_list[i] = 'F'
 
    return ''.join(temp_list)

# 关于是不是回文数这个问题自己一开始想傻了，忘记python可以直接利用字符串相等判断
def huiwen(x):
    if x==x[::-1]:
        return True
    else:
        return False

def add(x, X, num=0):
    if huiwen(x):
        print("STEP={}".format(num))
        return True
    else:
        y = x[::-1]   # 翻转，得到加数
        if X != 10:
            c = to_ten(x, X)+to_ten(y, X)
            c = ten_ToAny(X, c)   # 10进制加完之后在转换回去
        else:
            c = int(x) + y
        num += 1
        if num>30:
            print("Impossible!")
            return True
        else:
            return add(str(c), X, num)     # 采用递归的思想，因为要加很多步嘛，很自然的想法

if __name__ == "__main__":
    N = input()    # 进制数
    M = input()    # 数值
    add(M, N)
    ### 代码稍微写的有点复杂，懒得重构了