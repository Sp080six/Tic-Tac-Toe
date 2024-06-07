from tkinter import *
from tkinter import messagebox
import os
f=open("Score.txt")

root1=Tk()
root1.title("Tic-Tac-Toe")
root1.geometry("620x550")
root1.configure(bg="cadetblue")

t=open("Name.txt")
b=t.readlines()
pX=b[len(b)-2]
pO=b[len(b)-1]
t.close()

scoreX=0
scoreO=0

#X starts so true
clicked=True
count=0
#For disabling all the buttons
def disable():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
    b10=Button(root1,text="LEVEL-2",font=("Algerian",20),bg="lavender",fg= "black",command=level2)
    b10.place(x=165,y=420)
    l3.destroy()
    l4.destroy()
    l5=Label(root1,text=pX.rstrip('\n')+"(X): "+str(X),font=("Times New Roman",20),height=2,bg="cadetblue",fg="white")
    l5.place(x=400,y=60)
    l6=Label(root1,text=pO.rstrip('\n')+"(O): "+str(O),font=("Times New Roman",20),height=2,bg="cadetblue",fg="white")
    l6.place(x=400,y=120)

    
def level2():
    root1.destroy()
    os.system("Level2.py")
    
#To see if anyone won
def won():
    global winner
    global scoreX
    global scoreO
    global f
    global X
    global O
    
    winner=False
    #X Won
    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg="rosybrown")
        b2.config(bg="rosybrown")
        b3.config(bg="rosybrown")
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==0:
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            for i in range(len(a)):
                t.write(a[i])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
                
        f.close()
        t.close()
        f=open("Score.txt")
        a=f.readlines()
        for i in range(len(a)):
            X=a[len(a)-2]
            O=a[len(a)-1]
        
        f.close()
            
        messagebox.showinfo("Tic-Tac-Toe","Congratulations X wins")
        disable()
        
    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        b4.config(bg="rosybrown")
        b5.config(bg="rosybrown")
        b6.config(bg="rosybrown")
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==0:
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            for i in range(len(a)):
                t.write(a[i])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
                
        f.close()
        t.close()
        f=open("Score.txt")
        a=f.readlines()
        for i in range(len(a)):
            X=a[len(a)-2]
            O=a[len(a)-1]
        
        f.close()
        messagebox.showinfo("Tic-Tac-Toe","Congratulations X wins")
        disable()
    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        b7.config(bg="rosybrown")
        b8.config(bg="rosybrown")
        b9.config(bg="rosybrown")
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==0:
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            for i in range(len(a)):
                t.write(a[i])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
                
        f.close()
        t.close()
        f=open("Score.txt")
        a=f.readlines()
        for i in range(len(a)):
            X=a[len(a)-2]
            O=a[len(a)-1]
        
        f.close()
        messagebox.showinfo("Tic-Tac-Toe","Congratulations X wins")
        disable()
    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        b1.config(bg="rosybrown")
        b4.config(bg="rosybrown")
        b7.config(bg="rosybrown")
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==0:
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            for i in range(len(a)):
                t.write(a[i])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
                
        f.close()
        t.close()
        f=open("Score.txt")
        a=f.readlines()
        for i in range(len(a)):
            X=a[len(a)-2]
            O=a[len(a)-1]
        
        f.close()
        messagebox.showinfo("Tic-Tac-Toe","Congratulations X wins")
        disable()
    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        b2.config(bg="rosybrown")
        b5.config(bg="rosybrown")
        b8.config(bg="rosybrown")
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==0:
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            for i in range(len(a)):
                t.write(a[i])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
                
        f.close()
        t.close()
        f=open("Score.txt")
        a=f.readlines()
        for i in range(len(a)):
            X=a[len(a)-2]
            O=a[len(a)-1]
        
        f.close()
        messagebox.showinfo("Tic-Tac-Toe","Congratulations X wins")
        disable()
    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        b3.config(bg="rosybrown")
        b6.config(bg="rosybrown")
        b9.config(bg="rosybrown")
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==0:
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            for i in range(len(a)):
                t.write(a[i])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
                
        f.close()
        t.close()
        f=open("Score.txt")
        a=f.readlines()
        for i in range(len(a)):
            X=a[len(a)-2]
            O=a[len(a)-1]
        
        f.close()
        messagebox.showinfo("Tic-Tac-Toe","Congratulations X wins")
        disable()
    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        b1.config(bg="rosybrown")
        b5.config(bg="rosybrown")
        b9.config(bg="rosybrown")
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==0:
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            for i in range(len(a)):
                t.write(a[i])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
                
        f.close()
        t.close()
        f=open("Score.txt")
        a=f.readlines()
        for i in range(len(a)):
            X=a[len(a)-2]
            O=a[len(a)-1]
        
        f.close()
        messagebox.showinfo("Tic-Tac-Toe","Congratulations X wins")
        disable()
    elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        b3.config(bg="rosybrown")
        b5.config(bg="rosybrown")
        b7.config(bg="rosybrown")
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==0:
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            for i in range(len(a)):
                t.write(a[i])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
                
        f.close()
        t.close()
        f=open("Score.txt")
        a=f.readlines()
        for i in range(len(a)):
            X=a[len(a)-2]
            O=a[len(a)-1]
        
        f.close()
        messagebox.showinfo("Tic-Tac-Toe","Congratulations X wins")
        disable()
    #O won
    elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        b1.config(bg="goldenrod")
        b2.config(bg="goldenrod")
        b3.config(bg="goldenrod")
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==0:
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            for i in range(len(a)):
                t.write(a[i])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
                
        f.close()
        t.close()
        f=open("Score.txt")
        a=f.readlines()
        for i in range(len(a)):
            X=a[len(a)-2]
            O=a[len(a)-1]
        
        f.close()
        messagebox.showinfo("Tic-Tac-Toe","Congratulations O wins")
        disable()
    elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        b4.config(bg="goldenrod")
        b5.config(bg="goldenrod")
        b6.config(bg="goldenrod")
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==0:
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            for i in range(len(a)):
                t.write(a[i])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
                
        f.close()
        t.close()
        f=open("Score.txt")
        a=f.readlines()
        for i in range(len(a)):
            X=a[len(a)-2]
            O=a[len(a)-1]
        
        f.close()
        messagebox.showinfo("Tic-Tac-Toe","Congratulations O wins")
        disable()
    elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        b7.config(bg="goldenrod")
        b8.config(bg="goldenrod")
        b9.config(bg="goldenrod")
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==0:
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            for i in range(len(a)):
                t.write(a[i])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
                
        f.close()
        t.close()
        f=open("Score.txt")
        a=f.readlines()
        for i in range(len(a)):
            X=a[len(a)-2]
            O=a[len(a)-1]
        
        f.close()
        messagebox.showinfo("Tic-Tac-Toe","Congratulations O wins")
        disable()
    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        b1.config(bg="goldenrod")
        b4.config(bg="goldenrod")
        b7.config(bg="goldenrod")
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==0:
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            for i in range(len(a)):
                t.write(a[i])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
                
        f.close()
        t.close()
        f=open("Score.txt")
        a=f.readlines()
        for i in range(len(a)):
            X=a[len(a)-2]
            O=a[len(a)-1]
        
        f.close()
        messagebox.showinfo("Tic-Tac-Toe","Congratulations O wins")
        disable()
    elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        b2.config(bg="goldenrod")
        b5.config(bg="goldenrod")
        b8.config(bg="goldenrod")
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==0:
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            for i in range(len(a)):
                t.write(a[i])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
                
        f.close()
        t.close()
        f=open("Score.txt")
        a=f.readlines()
        for i in range(len(a)):
            X=a[len(a)-2]
            O=a[len(a)-1]
        
        f.close()
        messagebox.showinfo("Tic-Tac-Toe","Congratulations O wins")
        disable()
    elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        b3.config(bg="goldenrod")
        b6.config(bg="goldenrod")
        b9.config(bg="goldenrod")
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==0:
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            for i in range(len(a)):
                t.write(a[i])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
                
        f.close()
        t.close()
        f=open("Score.txt")
        a=f.readlines()
        for i in range(len(a)):
            X=a[len(a)-2]
            O=a[len(a)-1]
        
        f.close()
        messagebox.showinfo("Tic-Tac-Toe","Congratulations O wins")
        disable()
    elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        b1.config(bg="goldenrod")
        b5.config(bg="goldenrod")
        b9.config(bg="goldenrod")
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==0:
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            for i in range(len(a)):
                t.write(a[i])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
                
        f.close()
        t.close()
        f=open("Score.txt")
        a=f.readlines()
        for i in range(len(a)):
            X=a[len(a)-2]
            O=a[len(a)-1]
        
        f.close()
        messagebox.showinfo("Tic-Tac-Toe","Congratulations O wins")
        disable()
    elif b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
        b3.config(bg="goldenrod")
        b5.config(bg="goldenrod")
        b7.config(bg="goldenrod")
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==0:
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            for i in range(len(a)):
                t.write(a[i])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
                
        f.close()
        t.close()
        f=open("Score.txt")
        a=f.readlines()
        for i in range(len(a)):
            X=a[len(a)-2]
            O=a[len(a)-1]
        
        f.close()
        messagebox.showinfo("Tic-Tac-Toe","Congratulations O wins")
        disable()
    if count==9 and winner==False:
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==0:
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            for i in range(len(a)):
                t.write(a[i])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
                
        f.close()
        t.close()
        f=open("Score.txt")
        a=f.readlines()
        for i in range(len(a)):
            X=a[len(a)-2]
            O=a[len(a)-1]
        
        f.close()
        messagebox.showinfo("Tic-Tac-Toe","It's a tie..Hence no one wins!")
        disable()
        

def click(b):
    global clicked,count
    #Note:-if u want the text we can use the below statement if u want to get the word abcd,(b)label.config(text="abcd")
    if b["text"]==" " and clicked==True:
        b["text"]="X"
        clicked=False
        count=count+1
        won()
    elif b["text"]==" " and clicked==False:
        b["text"]="O"
        clicked=True
        count=count+1
        won()
    else:
        messagebox.showerror("Tic-Tac-Toe","The box has already been selected\nPlease select another box")

l1=Label(root1,text="LEVEL-1",font=("Algerian",25),bg="cadetblue",fg="white")
l1.place(x=180,y=10)
l2=Label(root1,text="SCORE:",font=("Algerian",22),height=2,bg="cadetblue",fg="white")
l2.place(x=400,y=10)

l3=Label(root1,text=pX.rstrip('\n')+"(X): 0",font=("Times New Roman",20),height=2,bg="cadetblue",fg="white")
l3.place(x=400,y=60)
l4=Label(root1,text=pO.rstrip('\n')+"(O): 0",font=("Times New Roman",20),height=2,bg="cadetblue",fg="white")
l4.place(x=400,y=120)


#Note:Lambda is used to for anything(variable) to be passed into a function
b1=Button(root1,text=" ",font=("Times New Roman",20),height=2,width=4,bg="SystemButtonFace",command=lambda:click(b1))
b2=Button(root1,text=" ",font=("Times New Roman",20),height=2,width=4,bg="SystemButtonFace",command=lambda:click(b2))
b3=Button(root1,text=" ",font=("Times New Roman",20),height=2,width=4,bg="SystemButtonFace",command=lambda:click(b3))

b4=Button(root1,text=" ",font=("Times New Roman",20),height=2,width=4,bg="SystemButtonFace",command=lambda:click(b4))
b5=Button(root1,text=" ",font=("Times New Roman",20),height=2,width=4,bg="SystemButtonFace",command=lambda:click(b5))
b6=Button(root1,text=" ",font=("Times New Roman",20),height=2,width=4,bg="SystemButtonFace",command=lambda:click(b6))

b7=Button(root1,text=" ",font=("Times New Roman",20),height=2,width=4,bg="SystemButtonFace",command=lambda:click(b7))
b8=Button(root1,text=" ",font=("Times New Roman",20),height=2,width=4,bg="SystemButtonFace",command=lambda:click(b8))
b9=Button(root1,text=" ",font=("Times New Roman",20),height=2,width=4,bg="SystemButtonFace",command=lambda:click(b9))

b1.place(x=100,y=100)
b2.place(x=200,y=100)
b3.place(x=300,y=100)

b4.place(x=100,y=200)
b5.place(x=200,y=200)
b6.place(x=300,y=200)

b7.place(x=100,y=300)
b8.place(x=200,y=300)
b9.place(x=300,y=300)

root1.mainloop()