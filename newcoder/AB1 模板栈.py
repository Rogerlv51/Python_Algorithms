## 手写一个栈的基本功能

# 请你实现一个栈。
# 操作：
# push x：将 加x\x 入栈，保证 x\x 为 int 型整数。
# pop：输出栈顶，并让栈顶出栈
# top：输出栈顶，栈顶不出栈




class stack():
    def __init__(self) -> None:
        self.item = []
    def isEmpty(self):
        return self.item == []
    def push(self, x):
        self.item.append(x)
    def pop(self):
        x = self.item.pop(-1)
        print(x)
    def top(self):
        print(self.item[-1])

if __name__ == "__main__":
    news = stack()
    n = eval(input())
    for i in range(n):
        temp = input()
        if temp[0:4] == "push":
            news.push(temp.split(" ")[1])
        if temp == "pop":
            if not news.isEmpty():
                news.pop()
            else:
                print("error")
        if temp == "top":
            if not news.isEmpty():
                news.top()
            else:
                print("error")