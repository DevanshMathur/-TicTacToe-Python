## Created By Devansh Mathur
class ExZero:

    def Memory (self):          ## TO initialize the variables          
        self.Player=["Player 1","Player 2"]
        self.d=('a','b','c','d','e','f','g','h','i') # DEFAULT ELEMENTS IN TUPLE
        self.u=[' ',' ',' ',' ',' ',' ',' ',' ',' '] # FOR USER CHOICES
        self.li=['a','b','c','d','e','f','g','h','i'] # For Computer (When we apply randon choice then list is needed to select possible moves)

    def Number (self):          ## TO ENTER NUMBER OF PLAYERS           
        while True :
            self.num = input("Enter Number of players 1 or 2 : ")
            if self.num.isdigit() and 1 <= int(self.num) <= 2:
                self.num=int(self.num)
                break
            print("Enter correct choice (1 or 2)")

    def Name (self):            ##  Taking Players Names                
        while True:
            ch=input("Do You Want to Enter Names(Y/N) : ")
            ch=ch.lower()
            if ch=='y':
                if self.num==1:
                    self.Player[0]=input("Enter The Name Of Player 1:").title().strip()
                    self.Player[1]="Computer"      
                    break

                elif self.num==2:
                    self.Player[0]=input("Enter The Name Of Player 1:").title().strip()
                    self.Player[1]=input("Enter The Name Of Player 2:").title().strip()

                    if self.Player[0]!=self.Player[1]:
                        break
                    else:
                        print("\nPlease Enter Different Names.")
                        
            elif ch=='n':
                print("\nWelcome to the Game.")
                if self.num==1:
                    self.Player[1]="Computer"
                break
                    
            print("\nEnter a Correct Choice.")
                                    
    def GUIName(self):          ##  Printing Players name               
        self.t.penup()
        self.t.goto(-100,200)
        self.t.color('Blue')
        self.t.write(f"{self.Player[0]:<25} : X",font=("Arial",16,"bold"))
        self.t.goto(-100,170)
        self.t.color('Red')
        self.t.write(f"{self.Player[1]:<25} : O",font=("Arial",16,"bold"))
        self.t.goto(-250,250)                 

    def CLIDraw(self):          ## Drawing Figure on CLI                
        print(f"\n{self.Player[0]} : X \t {self.Player[1]} : O")
        c=0
        for i in range(17):
            print(' '*30,end='')
            for j in range(32):
                if i in [2,8,14] and j in [4,16,25]:
                    if self.u[c]!=' ':
                        print(self.u[c],end='')
                    else:
                        print(self.d[c],end='')
                    c+=1
                else:
                    if i in [5,11]:
                        print("-",end='')
                    else:
                        if j in [10,21]:
                            print("|",end='')
                        else:
                            print(" ",end='')
            print()

    def GUIDraw(self):          ## Drawing Figure on GUI                
        x=[-50, 150 , 50, 150 , -150,50 , -150,-50]
        y=[-50,-150 , 50,-150 ,  150,50 ,  150,-50]
        self.t.color('black')
        self.t.pen(1)
        self.t.speed(0)
        for i in range(0,len(x),2):
            self.t.penup()
            self.t.goto(x[i],x[i+1])
            self.t.pendown()
            self.t.goto(y[i],y[i+1])
            self.t.penup()
        self.t.goto(-250,250)

    def Write(self):            ## FUNCTION TO PRINT CHANCES 
        count=-1
        co=[-100,0,100]
        self.t1.speed(0)
        self.t1.reset()
        self.t1.penup()
        for i in co:
            for j in co:
                count+=1
                if self.u[count]=='X':
                    self.t1.color('Blue')
                elif self.u[count]=='O':
                    self.t1.color('Red')
                else:
                    self.t1.color('black')
                self.t1.goto(j,-i)
                if self.u[count]!=' ':
                    self.t1.write(self.u[count],font=("Arial",16,"bold"))
                else:
                    self.t1.write(self.d[count],font=("Arial",16,"bold"))
        self.t1.goto(-250,250)
           

    def Play(self):             ## To Play the Chance                   
        for i in range(9):
            self.Turn (i)
            if self.type=='1':
                self.GUIDraw()
                self.Write()
            else:
                self.CLIDraw()
            print("\n\n")
            if i > 3:
                person=self.Win()  ## Person who win the Game
                if person != 0:
                    return person
        return person

    def Turn(self,i):           ## For Player turn                      
        flag=1
        while flag:
            flag=0
            tn=i%2      # tn=turn
            ch=self.Chance(i)
            if ch.isalpha()==0:
                print("Enter Correct Choice between A-I.")
                flag=1
            if flag==0:
                ch=ch.lower()
                if ch not in self.d:
                    print("Enter Correct Choice between A-I.")
                    flag=1
            if flag==0:
                ind=self.d.index(ch)
                val=self.Valid(ind)
                if val==0:
                    print(f"Enter Correct Choice That is Available {ch} is Not Available")
                    flag=1
            if flag==0:
                self.li.remove(ch)
                if tn==0:
                    self.u[ind]="X"
                else:
                    self.u[ind]="O"

    def Chance (self,i):        ## To take input for chance             
        tn=i%2
        if self.num==1:
            if tn==0:
                ch=input(f"chance : {self.Player[tn]} -> ")
            elif tn==1:
                ch=self.Comp(i)
                print(f"chance : {self.Player[tn]} -> {ch}")
        elif self.num==2:
            ch=input(f"chance : {self.Player[tn]} -> ")
        return ch    
       
    def Comp(self,i):           ## For computer turn                    
        from random import randint 
        ch=self.Check() # ch can be a-i or 'Z'
        if ch=="Z":
            ch=randint(0,len(self.li)-1)
            ch=self.li[ch]
        else:
            ch=self.d.index(ch)
            if self.u[ch]!=' ':
                ch=randint(0,len(self.li)-1)
                ch=self.li[ch]            
            else:
                ch=self.d[ch]
        return ch
        
    def Check(self):            ## To Check compute and user conditions 
        ch='Z'
        if self.u[0]==self.u[1]=='O' and self.u[2]!='X':
            ch=self.d[2]        
        if self.u[1]==self.u[2]=='O' and self.u[0]!='X':
            ch=self.d[0]
        if self.u[0]==self.u[2]=='O' and self.u[1]!='X':
            ch=self.u[1]
            
        if self.u[3]==self.u[4]=='O' and self.u[5]!='X':
            ch=self.d[5]        
        if self.u[4]==self.u[5]=='O' and self.u[3]!='X':
            ch=self.d[3]
        if self.u[5]==self.u[3]=='O' and self.u[4]!='X':
            ch=self.d[4]
        
        if self.u[6]==self.u[7]=='O' and self.u[8]!='X':
            ch=self.d[8]        
        if self.u[7]==self.u[8]=='O' and self.u[6]!='X':
            ch=self.d[6]
        if self.u[6]==self.u[8]=='O' and self.u[7]!='X':
            ch=self.d[7]
        
        if self.u[0]==self.u[3]=='O' and self.u[6]!='X':
            ch=self.d[6]
        if self.u[3]==self.u[6]=='O' and self.u[0]!='X':
            ch=self.d[0]
        if self.u[0]==self.u[6]=='O' and self.u[3]!='X':
            ch=self.d[3]
        
        if self.u[1]==self.u[4]=='O' and self.u[7]!='X':
            ch=self.d[7]
        if self.u[4]==self.u[7]=='O' and self.u[1]!='X':
            ch=self.d[1]
        if self.u[1]==self.u[7]=='O' and self.u[4]!='X':
            ch=self.d[4]
            
        if self.u[2]==self.u[5]=='O' and self.u[8]!='X':
            ch=self.d[8]
        if self.u[5]==self.u[8]=='O' and self.u[2]!='X':
            ch=self.d[2]
        if self.u[2]==self.u[8]=='O' and self.u[5]!='X':
            ch=self.d[5]
        
        if self.u[0]==self.u[4]=='O' and self.u[8]!='X':
            ch=self.d[8]
        if self.u[4]==self.u[8]=='O' and self.u[0]!='X':
            ch=self.d[0]
        if self.u[0]==self.u[8]=='O' and self.u[4]!='X':
            ch=self.d[4]
        
        if self.u[2]==self.u[4]=='O' and self.u[6]!='X':
            ch=self.d[6]
            
        if self.u[4]==self.u[6]=='O' and self.u[2]!='X':
            ch=self.d[2]
        if self.u[2]==self.u[6]=='O' and self.u[4]!='X':
            ch=self.d[4]
        
        if ch=='Z':
            if self.u[0]==self.u[1]=='X' and self.u[2]!='O':
                ch=self.d[2]        
            if self.u[1]==self.u[2]=='X' and self.u[0]!='O':
                ch=self.d[0]
            if self.u[0]==self.u[2]=='X' and self.u[1]!='O':
                ch=self.d[1]
                
            if self.u[3]==self.u[4]=='X' and self.u[5]!='O':
                ch=self.d[5]        
            if self.u[4]==self.u[5]=='X' and self.u[3]!='O':
                ch=self.d[3]
            if self.u[5]==self.u[3]=='X' and self.u[4]!='O':
                ch=self.d[4]
            
            if self.u[6]==self.u[7]=='X' and self.u[8]!='O':
                ch=self.d[8]        
            if self.u[7]==self.u[8]=='X' and self.u[6]!='O':
                ch=self.d[6]
            if self.u[6]==self.u[8]=='X' and self.u[7]!='O':
                ch=self.d[7]
            
            if self.u[0]==self.u[3]=='X' and self.u[6]!='O':
                ch=self.d[6]
            if self.u[3]==self.u[6]=='X' and self.u[0]!='O':
                ch=self.d[0]
            if self.u[0]==self.u[6]=='X' and self.u[3]!='O':
                ch=self.d[3]
            
            if self.u[1]==self.u[4]=='X' and self.u[7]!='O':
                ch=self.d[7]
            if self.u[4]==self.u[7]=='X' and self.u[1]!='O':
                ch=self.d[1]
            if self.u[1]==self.u[7]=='X' and self.u[4]!='O':
                ch=self.d[4]
                
            if self.u[2]==self.u[5]=='X' and self.u[8]!='O':
                ch=self.d[8]
            if self.u[5]==self.u[8]=='X' and self.u[2]!='O':
                ch=self.d[2]
            if self.u[2]==self.u[8]=='X' and self.u[5]!='O':
                ch=self.d[5]
            
            if self.u[0]==self.u[4]=='X' and self.u[8]!='O':
                ch=self.d[8]
            if self.u[4]==self.u[8]=='X' and self.u[0]!='O':
                ch=self.d[0]
            if self.u[0]==self.u[8]=='X' and self.u[4]!='O':
                ch=self.d[4]
            
            if self.u[2]==self.u[4]=='X' and self.u[6]!='O':
                ch=self.d[6]
            if self.u[4]==self.u[6]=='X' and self.u[2]!='O':
                ch=self.d[2]
            if self.u[2]==self.u[6]=='X' and self.u[4]!='O':
                ch=self.d[4]
        return ch

    def Valid(self,ind):        ## To CHECK THE CORRECTNESS OF INPUT    
        if self.u[ind] == ' ':
            return 1
        return 0

    def CLIWinner(self,per):    ## FUNCTION TO PRINT WINNER in CLI      
        if per==0:
            print("Match Draw")
        else:
            if per == "X":
                pr=0
            else:
                pr=1
            if self.num==2:
    
                print(f"Congratulations {self.Player[pr]}! \n You Win the Game")
            else:
                if pr==1:
                    
                    print("You Lose\nComputer Win the Game")
                else:
                    
                    print(f"Congratulations {self.Player[pr]}! \n You Win the Game")

    def GUIWinner(self,per):    ## FUNCTION TO PRINT WINNER in GUI      
        if per==0:
            self.t.goto(-200,-200)
            self.t.write("Match Draw",font=("Arial",16,"bold"))
        else:
            if per == "X":
                pr=0
            else:
                pr=1
            self.t.goto(-200,-200)
            self.t.color("Green")
            if self.num==2:
                self.t.write(f"Congratulations {self.Player[pr]}! \n You Win the Game",font=("Arial",16,"bold"))
            else:
                if pr==1:
                    self.t.write("You Lose\nComputer Win the Game",font=("Arial",16,"bold"))
                else:
                    self.t.write(f"Congratulations {self.Player[pr]}! \n You Win the Game",font=("Arial",16,"bold"))
       
    def Win(self):              ## To CHECK FOR WINNING SWITCHWATION    
        if self.u[0]==self.u[1]==self.u[2]!=' ':
            return self.u[0]
        
        elif self.u[3]==self.u[4]==self.u[5]!=' ':
            return self.u[3]
        
        elif self.u[6]==self.u[7]==self.u[8]!=' ':
            return self.u[6]
        
        elif self.u[0]==self.u[3]==self.u[6]!=' ':
            return self.u[0]
        
        elif self.u[1]==self.u[4]==self.u[7]!=' ':
            return self.u[1]
        
        elif self.u[2]==self.u[5]==self.u[8]!=' ':
            return self.u[2]
        
        elif self.u[0]==self.u[4]==self.u[8]!=' ':
            return self.u[0]
        
        elif self.u[2]==self.u[4]==self.u[6]!=' ':
            return self.u[2]
        return 0
        
    def CLI(self):              ## Without Turtle                       
        print("\t\t\t\tTic-Tac-Toe")
        self.Memory()
        self.Number()
        self.Name()
        self.CLIDraw()
        self.CLIWinner(self.Play())

    def GUI(self):
        import turtle
        self.t=turtle.Pen()
        self.t1=turtle.Pen()
        self.Memory()
        self.Number()
        self.Name()       
        self.GUIName()                 
        self.GUIDraw()
        self.Write()
        self.GUIWinner(self.Play())
        sleep(5)
        self.t.clear()
        self.t1.clear()        


    def Start(self):
        while True:
            self.type=input("Press 1 for GUI and 2 for CLI and 0 For exit : ")
            if self.type=='0':
                print("See you again :-)")
                print("Created by Devansh Mathur")
                sleep(7)
                break
            elif self.type=='1':
                self.GUI()
                print()
            elif self.type=='2':
                self.CLI()
                print()
            else:
                print("Enter valid choice\n")
if __name__=="__main__":
    from time import sleep
    A=ExZero()
    A.Start()
