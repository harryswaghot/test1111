# 创建列表，用中括号[] 实现，中括号内写入列表内容，用逗号隔开
"""创建列表元素"""
name_list = ["张三", "李四", "王五"]

"""查询列表元素"""
# 查询列表排位的元素。在列表的括号中写上位数,第一位为0，往后n+1。
print(name_list[0])

"""索引、修改列表元素"""
# 列表索引。用index函数在列表中中括号内输入元素内容进行索引，查询元素在列表中的排位，第一位是0，真实排位是 n+1
# 修改列表元素。 列表中口号中根据输入的位数 右边加等号 跟上要修改的元素内容
name_list[name_list.index("张三")] = "zhangsan"

# 打印查询修改的元素。 外部使用print函数
print(name_list[name_list.index("zhangsan")])

"""增加列表元素"""

# 使用 append方法可以向列表的末尾追加元素。
name_list.append("大老板")

# 使用 insert方法 可以在列表中任意位置插入元素，需要在插入的元素前加上排序数字并都逗号隔开
name_list.insert(0, "小不点")

# 使用extend方法。可以使两个列表合并
temp_list1 = ["张三丰", "汪峰"]
name_list.extend(temp_list1)

""" 删除列表中的元素"""

# 用 remove方法删去列表元素中的具体某个元素，需要在中括号[]中带上元素，如果列表中有重复的参数，默认删除第一个重复的。
name_list.remove("大老板")

# 用pop方法可以默认把列表中最后一个元素删除，删除具体元素在中括号内[]输入元素位置
name_list.pop(0)

# 用clear方法可以清空整个列表
name_list.clear()

# del函数删除变量，除了用列表中的方法，用del也可以删除，通常是用来删除变量的。一旦删除后续的代码不能再使用被删除的变量。
# 日常开发中要从列表删除数据还是建议使用列表中的方法删除。
a = "abc"
del a

list1 = ["孙悟空", "猪八戒", "沙师弟",  "唐三藏", "唐三藏", "白骨精", "红孩儿", "二郎神", "玉皇大帝", "太上老君"]
del list1[1]
print(list1)
"""下面的print(name_list)是给上面所有代码提供结果的"""
print(name_list)

"""len的使用"""
# len函数是查询列表中有多少个元素。 语法:len() 小括号内带上列表名称
print(name_list)
len_list = len(list1)
print("列表中有%d个元素" % len_list)

# 用count函数可以统计列表中重复元素的次数。中括号()内放上元素名
count = list1.count("唐三藏")
print("列表中出现了%d次" % count)

# 升序排列使用sort方法，从小到大排序
name1_list = ["zhangsan", "lisi", "wangwu"]
num_list = [2, 0, 9, 6, 7, 3, 1]
# name1_list.sort()
# num_list.sort()

# 降序使用sort方法，中括号()中 reverse=True，从大到小排列
num_list.sort(reverse=True)
name1_list.sort(reverse=True)

# 倒序、反转使用reverse() 中括号留空
num_list.reverse()
print(name1_list)
print(num_list)















