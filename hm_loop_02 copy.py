# 条件和循环练习题

# 题目1：输出 1-100 偶数和
i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
       sum += i
    i += 1
print(sum)

# 题目2：列出10行10列 *
row = 1
while row <= 10:
    col = 1
    while col <= 10:
        print("*", end="\t")
        col += 1
    print("")
    row += 1
# 题目3：输出直角三角形
i = 1
while i <= 10:
    print("*" * i)
    i += 1
# 题目4： 99乘法表
a = 1
while a <= 9:
    b = 1
    while b <= a:
        print("%d x %d =%d" % (b, a, (a * b),), end=" \t")
        b += 1
    print("")
    a += 1
# 题目5：让用户输入一个数字，判断这个数能否被1-100之间的数字整除
a = int(input("请输入一个整数："))
if (a > 0
    and a <= 100):
    for i in range(1, 100):
        if i % a == 0:
            print("%d可以被%d整除" % (a, i))
else:
    print("非法输入")

# 题目6：请用户输入数字，求和，直到输出0退出
sum = 0
while True:
    num = int(input("请输入一个数字:"))
    if num == 0:
        print("已结束")
        break
    else:
        sum += num
        print("当前总计:%d" % sum)

# 题目7：1、2、3、4能组成多少个互相不相同且不重复的三位数字？各是多少？
count = 0
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            if a != b and b != c and c != a:
                print(a, b, c)
                count += 1
print("能组成%d组不能的数字" % count)
# 题目8：求 1-100内所有的质数
b = []
for i in range(2, 101):
    f = True
    for ii in range(2, i-1):
        if i % ii == 0:
            f = False
            break
    if f == True:
        b.append(i)
print(b)

# 题目9： 随便输入一个串整数，请用循环把数字从反打出来。如 12345 打印出 54321
num = input("请输入数字:")
for i in num[::-1]:
    print(i, end="")


