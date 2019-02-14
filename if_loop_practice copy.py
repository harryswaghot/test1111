# 有A,B两个人随机随机生成一个1-10范围的数字进行比大小，谁大谁赢。共比较100000次，分别计算出A,B的胜率和平局的次数。

# 1.导入随机生成数字范围的包，并编写代码。

import random

# 2.循环比较100000次，再分别定义三个变量记录针对 A,B赢的次数和平局次数做记录

i = 0

A_win = 0

B_win = 0

tie = 0


while i < 100000:

    player_A = random.randint(1, 10)

    player_B = random.randint(1, 10)

    if player_A > player_B:

        A_win += 1

    elif player_A < player_B:

        B_win += 1

    else:

        tie += 1

    i += 1

# 3.调用玩家分别赢的次数，百分比统计后输出。

if A_win > B_win:

    print("玩家A的赢率是 %.2f%%, 玩家B的赢率是 %.2f%% -- 玩家A胜出 " % ((A_win / 1000), (B_win / 1000)))

elif A_win < B_win:

    print("玩家A的赢率是 %.2f%%, 玩家B的赢率是 %.2f%%-- 玩家B胜出 "  % ((A_win / 1000), (B_win / 1000)))

print("平局的概率是 %.2f%%" % (tie / 1000))

