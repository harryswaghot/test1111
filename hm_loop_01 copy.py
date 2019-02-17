
choice = input("请选择要打印的图形类，长方形选A ，正方形选B ，右倾矩形选C ，左边倾三角形选D, 直角三角形选E。请选择:")
if choice == "A":
    print("您要打印的图形是长方形")
    wide = int(input("请输入长方形的宽:"))
    height = int(input("请输入长方形的高:"))
    if wide != height:
        row = 1
        while row <= height:
            col = 1
            while col <= wide:
                print("*", end="")
                col += 1
            row += 1
            print("")
    else:
        print("长和宽不能相等")
elif choice == "B":
    print("您要打印的图形是正方形方形")
    length = int(input("请输入边长:"))
    row = 1
    while row <= length:
        print("*" * length)
        row += 1
elif choice == "C":
    print("您要打印的图形是左倾矩形")
    wide = int(input("请输入宽:"))
    height = int(input("请输入高:"))
    row = 1
    while row <= height:
        space = height
        while space > row:
            print(" ", end="")
            space -= 1
        col = 1
        while col <= wide:
            print("*", end="")
            col += 1
        print("")
        row += 1
elif choice == "D":
    print("您要打印的图形是右倾矩形")
    wide = int(input("请输入宽:"))
    height = int(input("请输入高:"))
    row = 1
    while row <= height:
        space = 1
        while space < row:
            print(" ", end="")
            space += 1
        col = 1
        while col <= wide:
            print("*", end="")
            col += 1
        print("")
        row += 1
elif choice == "E":
    print("您要打印的图形是直角三角形")
    height = int(input("请输入高:"))

    i = 1
    while i <= height:
        print("*" * i)
        i += 1

else:
    print("非法输入，请重新选择")














