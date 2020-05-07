## Created By Devansh Mathur

                #### TO ENTER NUMBER OF PLAYERS ####

def number():
    flag=1
    while flag :
        flag=0
        num=input("Enter Number of players : ")
        if num.isdigit():
            num=int(num)
            if 1 <= num <= 2:
                return num
        print("Enter correct choice (1 or 2)")
        flag=1
        


   
                #### FOR TAKING NAME AND NO OF PLAYERS ####

def name(num):

    global Player
    flag=1
    while flag:
        flag=0
        ch=input("Do You Want to Enter Names(Y/N) : ")
        ch=ch.lower()
        if ch=='y':
            if num==1:
                Player[0]=input("Enter The Name Of Player 1:").title()
                Player[1]="computer".title()      #title for capatial first alphabet

            elif num==2:
                Player[0]=input("Enter The Name Of Player 1:").title().strip()
                Player[1]=input("Enter The Name Of Player 2:").title().strip()

                if Player[0].strip()==Player[1].strip():
                    print("\nPlease Enter Different Names.")
                    flag=1

        elif ch=='n':
            print("\nWelcome to the Game.")
            if num==1:
                Player[1]="computer".title()      #title for capatial first alphabet
                
        else:
            print("\nEnter a Correct Choice.")
            flag=1

        if flag==0:           
                
            t.penup()
            t.goto(-100,200)
            print(f"\n{Player[0]} : X \t {Player[1]} : O")
            t.write(f"{Player[0]:<25} : X",font=("Arial",16,"bold"))
            t.goto(-100,170)
            t.write(f"{Player[1]:<25} : O",font=("Arial",16,"bold"))
            t.goto(-250,250)                 



                #### FUNCTION TO DRAW FIG ####
        
def draw ():
    x=[-50, 150 , 50, 150 , -150,50 , -150,-50]
    y=[-50,-150 , 50,-150 ,  150,50 ,  150,-50]
    t.color('black')
    t.pen(1)
    t.speed(0)
    for i in range(0,len(x),2):
        t.penup()
        t.goto(x[i],x[i+1])
        t.pendown()
        t.goto(y[i],y[i+1])
        t.penup()
    t.goto(-250,250)


                #### FUNCTION TO PRINT CHANCES ####
    
def write():
    count=-1
    co=[-100,0,100]
    t1.speed(0)
    t1.reset()
    t1.penup()
    for i in co:
        for j in co:
            count+=1
            if u[count]=='X':
                t1.color('red')
            elif u[count]=='O':
                t1.color('blue')
            else:
                t1.color('black')
            t1.goto(j,-i)
            if u[count]!=' ':
                t1.write(u[count],font=("Arial",16,"bold"))
            else:
                t1.write(d[count],font=("Arial",16,"bold"))
    t1.goto(-250,250)



                #### TO PLAY CHANCES ####
    
def play():
    for i in range(9):
        turn(i)
        write()
        
        if i>3:
            per=win() #PERSON WHO WIN
            if per=="X" or per=="O":
                return per
    return per
            
                
                #### TO GIVE TURN ####
            
def turn(i):
    global u
    global li
    flag=1
    while flag:
        flag=0
        tn=i%2      # tn=turn
        ch=chance(i)
        if ch.isalpha()==0:
            print("Enter Correct Choice between A-I.")
            flag=1
        
        if flag==0:
            ch=ch.lower()
            if ch not in d:
                print("Enter Correct Choice between A-I.")
                flag=1
        if flag==0:
            ind=d.index(ch)
            val=valid(ind)
            if val==0:
                print(f"Enter Correct Choice That is Available {ch} is Not Available")
                flag=1
        if flag==0:
            li.remove(ch)
            if tn==0:
                u[ind]="X"
            else:
                u[ind]="O"


                #### TO TAKE INPUT CHANCE ####
        
def chance(i):
    global num
    tn=i%2
    if num==1:
        if tn==0:
            ch=input(f"chance : {Player[tn]} -> ")
        elif tn==1:
            ch=comp(i)
            print(f"chance : {Player[tn]} -> {ch}")
    elif num==2:
        ch=input(f"chance : {Player[tn]} -> ")
    return ch    

    
                #### TO TAKE INPUT FROM COMPUTER ####
def comp(i):
    global li
    ch=check() # ch can be a-i or 'Z'
   
    if ch=="Z":
        ch=randint(0,len(li)-1)
        ch=li[ch]
    else:
        ch=d.index(ch)
        if u[ch]!=' ':
            ch=randint(0,len(li)-1)
            ch=li[ch]            
        else:
            ch=d[ch]
    return ch
    
                #### TO CHECK USER WIN CONDITION ####
def check():
    ch='Z'
    if u[0]==u[1]=='O' and u[2]!='X':
        ch=d[2]        
    if u[1]==u[2]=='O' and u[0]!='X':
        ch=d[0]
    if u[0]==u[2]=='O' and u[1]!='X':
        ch=u[1]
        
    if u[3]==u[4]=='O' and u[5]!='X':
        ch=d[5]        
    if u[4]==u[5]=='O' and u[3]!='X':
        ch=d[3]
    if u[5]==u[3]=='O' and u[4]!='X':
        ch=d[4]
    
    if u[6]==u[7]=='O' and u[8]!='X':
        ch=d[8]        
    if u[7]==u[8]=='O' and u[6]!='X':
        ch=d[6]
    if u[6]==u[8]=='O' and u[7]!='X':
        ch=d[7]
    
    if u[0]==u[3]=='O' and u[6]!='X':
        ch=d[6]
    if u[3]==u[6]=='O' and u[0]!='X':
        ch=d[0]
    if u[0]==u[6]=='O' and u[3]!='X':
        ch=d[3]
    
    if u[1]==u[4]=='O' and u[7]!='X':
        ch=d[7]
    if u[4]==u[7]=='O' and u[1]!='X':
        ch=d[1]
    if u[1]==u[7]=='O' and u[4]!='X':
        ch=d[4]
        
    if u[2]==u[5]=='O' and u[8]!='X':
        ch=d[8]
    if u[5]==u[8]=='O' and u[2]!='X':
        ch=d[2]
    if u[2]==u[8]=='O' and u[5]!='X':
        ch=d[5]
    
    if u[0]==u[4]=='O' and u[8]!='X':
        ch=d[8]
    if u[4]==u[8]=='O' and u[0]!='X':
        ch=d[0]
    if u[0]==u[8]=='O' and u[4]!='X':
        ch=d[4]
    
    if u[2]==u[4]=='O' and u[6]!='X':
        ch=d[6]
        
    if u[4]==u[6]=='O' and u[2]!='X':
        ch=d[2]
    if u[2]==u[6]=='O' and u[4]!='X':
        ch=d[4]
    
    if ch=='Z':
        if u[0]==u[1]=='X' and u[2]!='O':
            ch=d[2]        
        if u[1]==u[2]=='X' and u[0]!='O':
            ch=d[0]
        if u[0]==u[2]=='X' and u[1]!='O':
            ch=d[1]
            
        if u[3]==u[4]=='X' and u[5]!='O':
            ch=d[5]        
        if u[4]==u[5]=='X' and u[3]!='O':
            ch=d[3]
        if u[5]==u[3]=='X' and u[4]!='O':
            ch=d[4]
        
        if u[6]==u[7]=='X' and u[8]!='O':
            ch=d[8]        
        if u[7]==u[8]=='X' and u[6]!='O':
            ch=d[6]
        if u[6]==u[8]=='X' and u[7]!='O':
            ch=d[7]
        
        if u[0]==u[3]=='X' and u[6]!='O':
            ch=d[6]
        if u[3]==u[6]=='X' and u[0]!='O':
            ch=d[0]
        if u[0]==u[6]=='X' and u[3]!='O':
            ch=d[3]
        
        if u[1]==u[4]=='X' and u[7]!='O':
            ch=d[7]
        if u[4]==u[7]=='X' and u[1]!='O':
            ch=d[1]
        if u[1]==u[7]=='X' and u[4]!='O':
            ch=d[4]
            
        if u[2]==u[5]=='X' and u[8]!='O':
            ch=d[8]
        if u[5]==u[8]=='X' and u[2]!='O':
            ch=d[2]
        if u[2]==u[8]=='X' and u[5]!='O':
            ch=d[5]
        
        if u[0]==u[4]=='X' and u[8]!='O':
            ch=d[8]
        if u[4]==u[8]=='X' and u[0]!='O':
            ch=d[0]
        if u[0]==u[8]=='X' and u[4]!='O':
            ch=d[4]
        
        if u[2]==u[4]=='X' and u[6]!='O':
            ch=d[6]
        if u[4]==u[6]=='X' and u[2]!='O':
            ch=d[2]
        if u[2]==u[6]=='X' and u[4]!='O':
            ch=d[4]
    return ch


                #### To CHECK THE CORRECTNESS OF INPUT ####
    
def valid(ind):
    if u[ind]==' ':
        return 1
    return 0


                #### FUNCTION TO PRINT WINNER ####

def winner(per):
    
    if per==0:
        print("Match Draw")
        t1.goto(-200,-200)
        t1.write("Match Draw",font=("Arial",16,"bold"))
    else:
        if per == "X":
            pr=0
        else:
            pr=1
        t1.goto(-200,-200)
        t1.color("Green")
        if num==2:
            t1.write(f"Congratulations {Player[pr]}! \n You Win the Game",font=("Arial",16,"bold"))
            print(f"Congratulations {Player[pr]}! \n You Win the Game")
        else:
            if pr==1:
                t1.write("You Lose\nComputer Win the Game",font=("Arial",16,"bold"))
                print("You Lose\nComputer Win the Game")
            else:
                t1.write(f"Congratulations {Player[pr]}! \n You Win the Game",font=("Arial",16,"bold"))
                print(f"Congratulations {Player[pr]}! \n You Win the Game")
                

#### To CHECK FOR WINNING SWITCHWATION ####
def win():
    if u[0]==u[1]==u[2]!=' ':
        return u[0]
    
    elif u[3]==u[4]==u[5]!=' ':
        return u[3]
    
    elif u[6]==u[7]==u[8]!=' ':
        return u[6]
    
    elif u[0]==u[3]==u[6]!=' ':
        return u[0]
    
    elif u[1]==u[4]==u[7]!=' ':
        return u[1]
    
    elif u[2]==u[5]==u[8]!=' ':
        return u[2]
    
    elif u[0]==u[4]==u[8]!=' ':
        return u[0]
    
    elif u[2]==u[4]==u[6]!=' ':
        return u[2]
    return 0
 
        
#### MAIN EXECUTION BEGIN ####

print("\t\t\t\tTic-Tac-Toe")
import turtle
from random import randint
Player=["Player 1","Player 2"]
num=number()
t=turtle.Pen()
t1=turtle.Pen()
t1.penup()
t1.goto(-250,250)
d=('a','b','c','d','e','f','g','h','i') # DEFAULT ELEMENTS IN TUPLE
u=[' ',' ',' ',' ',' ',' ',' ',' ',' '] # FOR USER CHOICES
li=['a','b','c','d','e','f','g','h','i'] # For Computer (When we apply randon choice then list is needed to select possible moves)
name(num)
draw()
write()
per=play()
winner(per)
    


