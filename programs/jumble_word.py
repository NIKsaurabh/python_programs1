import random
def choose():
    words=['computer','aeroplane','engineer','mathematics','keyboard','country','donation','opportunity','punishment','automatic','manual','communicate','eyebrow','icecream','peacock','helicopter']
    pick=random.choice(words)
    return pick
def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
def thankyou(p1n,p2n,p1s,p2s):
    print(p1n,", your score is : ",p1s)
    print(p2n,", your score is : ",p2s)
    
    
def play():
    p1name=input("Player 1, please enter your name\n")
    p2name=input("Player 2, please enter your name\n")
    p1s=0
    p2s=0
    turn=0
    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        print (qn)
        if turn%2==0:
            print(p1name,"your turn")
            ans=input("What is in my mind?\n")
            if ans==picked_word:
                p1s=p1s+1
                print("your score is : ",p1s)
            else:
                print("Better luck next time, I thought: ",picked_word)
            c=int(input("Press 1 to continue or 0 to quit : "))
            if c==0:
                thankyou(p1name,p2name,p1s,p2s)
                break
            
        else:
            print(p2name,"your turn")
            ans=input("What is in my mind?\n")
            if ans==picked_word:
                p2s=p2s+1
                print("your score is : ",p2s)
            else:
                print("Better luck next time, I thought: ",picked_word)
            c=int(input("Press 1 to continue or 0 to quit : "))
            if c==0:
                thankyou(p1name,p2name,p1s,p2s)
                break
        turn=turn+1
play()                
                
    