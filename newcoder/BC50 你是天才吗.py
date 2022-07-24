# KiKi想知道他自己是不是天才，请帮他编程判断。输入一个整数表示一个人的智商，
# 如果大于等于140，则表明他是一个天才，输出“Genius”

# 输入描述
# 多组输入

while True:
    try:
        n = int(input())
        if n >= 140:
            print('Genius')
    except:
        break