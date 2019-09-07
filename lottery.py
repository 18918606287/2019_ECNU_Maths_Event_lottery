import easygui as gui
import random
import time
import csv

#Load name list from csv file
csv_file = csv.reader(open('素材/名册.csv', 'r'))
pool = []
for number_name in csv_file:
    pool.append(number_name)
#move the title row
pool = pool[1:]
random.shuffle(pool)

#Parameters Initialization
lottery = []
visited = []
lottery_list = "三等奖：\n"
num_special = gui.integerbox(msg="设置锦鲤奖数量",title="抽奖数目设置",lowerbound=1,upperbound=100)
num_first = gui.integerbox(msg="设置一等奖数量",title="抽奖数目设置",lowerbound=1,upperbound=100)
num_second = gui.integerbox(msg="设置二等奖数量",title="抽奖数目设置",lowerbound=1,upperbound=100)
num_third = gui.integerbox(msg="设置三等奖数量",title="抽奖数目设置",lowerbound=1,upperbound=100)

#main program
while True:
    msg =  gui.buttonbox("","抽奖系统",("抽奖","退出"), "./素材/chou_jiang.gif")
    if msg == '抽奖' or msg == "./素材/chou_jiang.gif":
        mem = random.choice(pool)
        while mem in visited:
            #avoid duplicate candidates
            random.shuffle(pool)
            mem = random.choice(pool)
        visited.append(mem)
        re_lottery = gui.ccbox(msg="本次抽奖结果为："+str(mem[0])+" "+str(mem[1])+"\n"+"目前获奖情况为：\n"+str(lottery_list)+str(mem[0])+" "+str(mem[1])+"\n", title='抽奖成功', choices=("继续","本轮重抽"))
        while not re_lottery:
            mem = random.choice(pool)
            while mem in visited:
                mem = random.choice(pool)
            visited.append(mem)
            re_lottery = gui.ccbox(msg="本次抽奖结果为："+str(mem[0])+" "+str(mem[1])+"\n"+"目前获奖情况为：\n"+str(lottery_list)+str(mem[0])+" "+str(mem[1])+"\n", title='抽奖成功', choices=("继续","本轮重抽"))
        lottery.append(mem)
        lottery_list += str(mem[0])+" "+str(mem[1])+"\n"
        if len(lottery) == num_third:
            lottery_list += "二等奖：\n"
        if len(lottery) == num_third + num_second:
            lottery_list += "一等奖：\n"
        if len(lottery) == num_third + num_second + num_first:
            lottery_list += "锦鲤奖：\n"
        if len(lottery) >= num_first + num_second + num_third + num_special:
            #close the program after all candidates are seleceted
            end = gui.msgbox(msg = "全部抽奖已完成,程序将在30s后自动退出", title="自动关闭", ok_button="退出")
            if end == '退出':
                break
            time.sleep(30)
            break
    else:
        break
