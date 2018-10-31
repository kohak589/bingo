# -*- coding:utf-8 -*-
import random, sys
def randomNumber(check,seedValue=0):
    #{check==B:0,I:1,N:2,G:3,O:4}
    value = [n for n in range(check * 15 + 1,check * 15 +16)]
    random.seed(seedValue)
    random.shuffle(value)
    bingo = value[:5]
    return bingo

def makeNumber(sub):
    #判定の時に使う
    #subは(二回目以降の)seed値を変えるために使用
    a = [randomNumber(x,sub) for x in range(0,5)]
    number = [i for n in a for i in n]
    return number

def makeCard(number):
    card = [number[i:i+5] for i in range(0,25,5)]
    print("{Ｂ   Ｉ   Ｎ   Ｇ   Ｏ}")
    print("========================", end="")
    for n in range(0,5):
        print()
        for i in range(0,5):
            print("|" + str(card[i][n]).zfill(2)+ "|", end=" ")

def check(ballnumber):
    pos = yourNumber.index(ballnumber)
    yourNumber[pos] = "$$"
    return pos

def ball(nth):
    ballNumber = n[nth]
    print("====================")
    print(("[") + str(nth + 1) + "回目の番号は：" +str(ballNumber) + ("]"),end="  ")
    if ballNumber in yourNumber:
        global hit
        print("当たりました！")
        hit.append(check(ballNumber))
        #print(yourNumber)
    else:
        print("")
    print("====================")

def lineCheck(x):
    global BINGO 
    global reach
    point = 0
    # x=0,5,10,15,20
    if x in hit:
        point += 1
    if x+1 in hit:
        point += 1
    if x+2 in hit:
        point += 1
    if x+3 in hit:
        point += 1
    if x+4 in hit:
        point += 1
    if point == 5:
        BINGO += 1
    if point == 4:
        reach += 1

def rawCheck(x):
    global BINGO 
    global reach
    point = 0
    # x=0,1,2,3,4
    if x in hit:
        point += 1
    if x+5 in hit:
        point += 1
    if x+10 in hit:
        point += 1
    if x+15 in hit:
        point += 1
    if x+20 in hit:
        point += 1
    if point == 5:
        BINGO += 1
    if point == 4:
        reach += 1

def crossCheck1():
    global BINGO 
    global reach
    point = 0
    if 0 in hit:
        point += 1
    if 6 in hit:
        point += 1
    if 12 in hit:
        point += 1
    if 18 in hit:
        point += 1
    if 24 in hit:
        point += 1
    if point == 5:
        BINGO += 1
    if point == 4:
        reach += 1

def crossCheck2():
    global BINGO 
    global reach
    point = 0
    if 20 in hit:
        point += 1
    if 16 in hit:
        point += 1
    if 12 in hit:
        point += 1
    if 8 in hit:
        point += 1
    if 4 in hit:
        point += 1
    if point == 5:
        BINGO += 1
    if point == 4:
        reach += 1

def trueCheck(num):
    global BINGO
    global reach
    [lineCheck(x) for x in range(0,25,5)]
    [rawCheck(x) for x in range(0,5)]
    crossCheck1()
    crossCheck2()
    if BINGO >= 1:
        print("  ビンゴ！！", end="")
        gameOver = True
        return gameOver
    elif reach >= 1:
        print("  " +str(reach) + "リーチ！！", end="")
        reach = 0
        gameOver = False
        return gameOver
    else:
        gameOver = False
        return gameOver

def judge(x):
    print("")
    print("これまでにあなたは" + str(x) + "回かかりました！")
    five=float((x * (x-1) * (x-2) * (x-3) * (x-4)) / (75 * 74 * 73 * 72 * 71))
    if hard:
        probability = 1 - ((1-five) ** 12)
    else:
        four=float((x * (x-1) * (x-2) * (x-3)) / (75 * 74 * 73 * 72))
        probability = 1 - ((1-five) ** 8) * ((1-four) ** 4)
    print(str(probability * 100) + "%" )
    print("これは" + str(x) +"回目までにビンゴができる確率です！")
    print("あなたの運勢は・・・【", end=(""))
    if probability >= 0.95:
        print("大凶】")
    elif probability >= 0.85:
        print("凶】")
    elif probability >= 0.70:
        print("末吉】")
    elif probability >= 0.55:
        print("小吉】")
    elif probability >= 0.40:
        print("中吉】")
    elif probability >= 0.25:
        print("大吉】")
    elif probability >= 0.10:
        print("大大吉】")
    else:
        print("神】")
    

n = [n for n in range(1,76)]
some = random.random() * 100
print("ハード：FREEマスがないよ！")
print("ノーマル：FREEマスがあるよ！")
autoMode = False
while True:
    while True:
        if autoMode:
            print("オート切替(A)uto：現在オートon")
        else:
            print("オート切替(A)uto：現在オートoff")
        wait = input("ハードモードなら(H)ard、ノーマルモードなら(N)ormalを押してね！：").upper()
        if wait == "H":
            hard = True
            break
        elif wait == "N":
            hard = False
            break
        elif wait == "A" and not autoMode:
            autoMode = True
        elif wait == "A" and autoMode:
            autoMode = False
    some = random.random() * 100
    random.shuffle(n)
    reach = 0
    yourNumber = makeNumber(sub=some)
    if hard:
        hit = []
    else:
        hit = [12]
        yourNumber[12] = "$$"
    waitTurn = True
    x = 0
    BINGO = 0
    makeCard(yourNumber)
    print("ENTERキーを押す度に数字が選ばれるよ！")
    while waitTurn:
        if not autoMode:
            wait = input()
        else:
            print("")
        ball(x)
        makeCard(yourNumber)
        x += 1
        if trueCheck(hit):
            judge(x)
            while True:
                wait = input("やめるなら(Q)uit、続けるなら(R)esetを押してね！：").upper()
                if wait == "Q":
                    sys.exit(0)
                elif wait == "R":
                    waitTurn = False
                    break