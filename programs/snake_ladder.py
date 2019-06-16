from PIL import Image
import random
end=100
def show_board():
    img=Image.open("snake_ladder.png")
    img.show()

def check_ladder(point):
    if point==3:
        print("Ladder")
        return 20
    elif point==6:
        print('Ladder')
        return 14
    elif point==11:
        print('Ladder')
        return 28
    elif point==15:
        print('Ladder')
        return 34
    elif point==17:
        print('Ladder')
        return 74
    elif point==22:
        print('Ladder')
        return 37
    elif point==38:
        print('Ladder')
        return 59
    elif point==49:
        print('Ladder')
        return 67
    elif point==57:
        print('Ladder')
        return 76
    elif point==61:
        print('Ladder')
        return 78
    elif point==73:
        print('Ladder')
        return 86
    elif point==81:
        print('Ladder')
        return 98
    elif point==88:
        print('Ladder')
        return 91
    else:
        return point

def check_snake(point):
    if point==18:
        print('Snake')
        return 1
    elif point==8:
        print('Snake')
        return 4
    elif point==26:
        print('Snake')
        return 10
    elif point==39:
        print('Snake')
        return 5
    elif point==51:
        print('Snake')
        return 6
    elif point==54:
        print('Snake')
        return 36
    elif point==56:
        print('Snake')
        return 1
    elif point==60:
        print('Snake')
        return 23
    elif point==75:
        print('Snake')
        return 28
    elif point==83:
        print('Snake')
        return 45
    elif point==85:
        print('Snake')
        return 59
    elif point==90:
        print('Snake')
        return 48
    elif point==92:
        print('Snake')
        return 25
    elif point==97:
        print('Snake')
        return 87
    elif point==99:
        print('Snake')
        return 63
    else:
        return point
    
def reached_end(point):
    if point==end:
        return True
    else:
        return False
    
def play():
    p1_name=input("Player 1, enter your name")
    p2_name=input("Player 2, enter your name")
    pp1=0
    pp2=0
    turn=0
    
    while(1):
        if turn%2==0:
            print(p1_name," your turn")
            c=int(input("Press 1 to continue and 0 to quit"))
            if c==0:
                print(p1_name,' scored ',pp1)
                print(p2_name,' scored ',pp2)
                print('Quitting the game, Thanks for playing')
                break
            dice=random.randint(1,6)
            print('Dice showed ',dice)
            pp1=pp1+dice
            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)
            if pp1>end:
                pp1=end
            print(p1_name,' your score: ',pp1)
            if reached_end(pp1):
                print(p1_name,' won')
                break
        else:
            print(p2_name," your turn")
            c=int(input("Press 1 to continue and 0 to quit"))
            if c==0:
                print(p1_name,' scored ',pp1)
                print(p2_name,' scored ',pp2)
                print('Quitting the game, Thanks for playing')
                break
            dice=random.randint(1,6)
            print('Dice showed ',dice)
            pp2=pp2+dice
            pp2=check_ladder(pp2)
            pp2=check_snake(pp2)
            if pp2>end:
                pp2=end
            print(p2_name,' your score: ',pp2)
            if reached_end(pp2):
                print(p2_name,' won')
                break
        turn=turn+1 
show_board()
play()