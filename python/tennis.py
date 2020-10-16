#模拟球员比赛过程，计算两位球员分别的胜率
from random import *
def printintro() :
    print("这是一个根据球员能力计算球员获胜概率的模拟程序")

def getinputs():
    A = eval(input("Please input the A player ability:"))
    B = eval(input("Please input the B player ability:"))
    N = eval(input("please input the number of simulations:"))
    return A, B, N

def gameover(A, B) :
    return A == 15 or B == 15 

def sinonegames(A, B, N) :
    score_A, score_B = 0, 0
    serving = 'A'
    while not gameover(score_A, score_B) :
        if(serving == 'A') :
            if(random() < A):
                score_A += 1
            else :
                serving = 'B'
        else :
            if(random() < B) :
                score_B += 1
            else:
                serving = 'A'
    return score_A, score_B      

def singames(A, B, N):
    wins_A, wins_B = 0, 0
    for i in range(N) :
        score_A, score_B = sinonegames(A, B, N)
        if(score_A > score_B) :
            wins_A += 1
        elif(score_A < score_B) :
            wins_B += 1
        else:
            continue
    return wins_A, wins_B

def printsummary(winsA1, winsB1) :
    N = winsA1 + winsB1
    print('Games simulated:%d', N)
    print("\nwin for A:", winsA1, winsA1/N)
    print("\nwin for B:", winsB1, winsB1/N)
    
def main() :
    printintro()
    A_pro, B_pro, n = getinputs()
    winsA, winsB = singames(A_pro, B_pro, n)
    printsummary(winsA, winsB)
    
main()
    