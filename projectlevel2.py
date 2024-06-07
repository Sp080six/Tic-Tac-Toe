from tkinter import *
from tkinter import messagebox
import os
root=Tk()
root.title("Tic-Tac-Toe")
root.configure(bg="#E39FF6")
root.geometry("700x650")

f=open("Score.txt")
a=f.readlines()
X=a[len(a)-2]
O=a[len(a)-1]
f.close()
t=open("Name.txt")
b=t.readlines()
pX=b[len(b)-2]
pO=b[len(b)-1]
t.close()
f=open("Score.txt")

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
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)
    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)
    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)
    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)
    b25.config(state=DISABLED)
    b26=Button(root,text="LEVEL-3",font=("Algerian",20),bg="black",fg= "#E39FF6",command=level3)
    b26.place(x=250,y=540)
    l3.destroy()
    l4.destroy()
    l5=Label(root,text=pX.rstrip('\n')+"(X): "+str(X),font=("Times New Roman",20),height=2,bg="#E39FF6",fg="black")
    l5.place(x=500,y=100)
    l6=Label(root,text=pO.rstrip('\n')+"(O): "+str(O),font=("Times New Roman",20),height=2,bg="#E39FF6",fg="black")
    l6.place(x=500,y=150)

    
def level3():
    root.destroy()
    os.system("Level3.py")
#To see if anyone won
def won():
    global scoreX
    global scoreO
    global winner
    global f
    global X
    global O
    winner=False
    #X Won
    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X"and b4["text"]=="X" and b5["text"]=="X":
        b1.config(bg="#c0c0c0",fg="black")
        b2.config(bg="#c0c0c0",fg="black")
        b3.config(bg="#c0c0c0",fg="black")
        b4.config(bg="#c0c0c0",fg="black")
        b5.config(bg="#c0c0c0",fg="black")
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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
    elif b6["text"]=="X" and b7["text"]=="X" and b8["text"]=="X"and b9["text"]=="X" and b10["text"]=="X":
        b6.config(bg="#c0c0c0",fg="black")
        b7.config(bg="#c0c0c0",fg="black")
        b8.config(bg="#c0c0c0",fg="black")
        b9.config(bg="#c0c0c0",fg="black")
        b10.config(bg="#c0c0c0",fg="black")
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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
    elif b11["text"]=="X" and b12["text"]=="X" and b13["text"]=="X"and b14["text"]=="X" and b15["text"]=="X":
        b11.config(bg="#c0c0c0",fg="black")
        b12.config(bg="#c0c0c0",fg="black")
        b13.config(bg="#c0c0c0",fg="black")
        b14.config(bg="#c0c0c0",fg="black")
        b15.config(bg="#c0c0c0",fg="black")
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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
    elif b16["text"]=="X" and b17["text"]=="X" and b18["text"]=="X"and b19["text"]=="X" and b20["text"]=="X":
        b16.config(bg="#c0c0c0",fg="black")
        b17.config(bg="#c0c0c0",fg="black")
        b18.config(bg="#c0c0c0",fg="black")
        b19.config(bg="#c0c0c0",fg="black")
        b20.config(bg="#c0c0c0",fg="black")
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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
    elif b21["text"]=="X" and b22["text"]=="X" and b23["text"]=="X"and b24["text"]=="X" and b25["text"]=="X":
        b21.config(bg="#c0c0c0",fg="black")
        b22.config(bg="#c0c0c0",fg="black")
        b23.config(bg="#c0c0c0",fg="black")
        b24.config(bg="#c0c0c0",fg="black")
        b25.config(bg="#c0c0c0",fg="black")
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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
    elif b1["text"]=="X" and b6["text"]=="X" and b11["text"]=="X" and b16["text"]=="X" and b21["text"]=="X":
        b1.config(bg="#c0c0c0",fg="black")
        b6.config(bg="#c0c0c0",fg="black")
        b11.config(bg="#c0c0c0",fg="black")
        b16.config(bg="#c0c0c0",fg="black")
        b21.config(bg="#c0c0c0",fg="black")
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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
	
    elif b2["text"]=="X" and b7["text"]=="X" and b12["text"]=="X" and b17["text"]=="X" and b22["text"]=="X":
        b2.config(bg="#c0c0c0",fg="black")
        b7.config(bg="#c0c0c0",fg="black")
        b12.config(bg="#c0c0c0",fg="black")
        b17.config(bg="#c0c0c0",fg="black")
        b22.config(bg="#c0c0c0",fg="black")
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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
      
    elif b3["text"]=="X" and b8["text"]=="X" and b13["text"]=="X" and b18["text"]=="X" and b23["text"]=="X":
        b3.config(bg="#c0c0c0",fg="black")
        b8.config(bg="#c0c0c0",fg="black")
        b13.config(bg="#c0c0c0",fg="black")
        b18.config(bg="#c0c0c0",fg="black")
        b23.config(bg="#c0c0c0",fg="black")
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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

    elif b4["text"]=="X" and b9["text"]=="X" and b14["text"]=="X" and b19["text"]=="X" and b24["text"]=="X":
        b4.config(bg="#c0c0c0",fg="black")
        b9.config(bg="#c0c0c0",fg="black")
        b14.config(bg="#c0c0c0",fg="black")
        b19.config(bg="#c0c0c0",fg="black")
        b24.config(bg="#c0c0c0",fg="black")
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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

    elif b5["text"]=="X" and b10["text"]=="X" and b15["text"]=="X" and b20["text"]=="X" and b25["text"]=="X":
        b5.config(bg="#c0c0c0",fg="black")
        b10.config(bg="#c0c0c0",fg="black")
        b15.config(bg="#c0c0c0",fg="black")
        b20.config(bg="#c0c0c0",fg="black")
        b25.config(bg="#c0c0c0",fg="black")
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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
	
    
    elif b1["text"]=="X" and b7["text"]=="X" and b13["text"]=="X" and b19["text"]=="X" and b25["text"]=="X":
        b1.config(bg="#c0c0c0",fg="black")
        b7.config(bg="#c0c0c0",fg="black")
        b13.config(bg="#c0c0c0",fg="black")
        b19.config(bg="#c0c0c0",fg="black")
        b25.config(bg="#c0c0c0",fg="black") 
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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


    elif b5["text"]=="X" and b9["text"]=="X" and b13["text"]=="X" and b17["text"]=="X" and b21["text"]=="X":
        b5.config(bg="#c0c0c0",fg="black")
        b9.config(bg="#c0c0c0",fg="black")
        b13.config(bg="#c0c0c0",fg="black")
        b17.config(bg="#c0c0c0",fg="black")
        b21.config(bg="#c0c0c0",fg="black") 
        winner=True
        scoreX=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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
    elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O"and b4["text"]=="O" and b5["text"]=="O":
        b1.config(bg="white",fg="black")
        b2.config(bg="white",fg="black")
        b3.config(bg="white",fg="black")
        b4.config(bg="white",fg="black")
        b5.config(bg="white",fg="black")
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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
    elif b6["text"]=="O" and b7["text"]=="O" and b8["text"]=="O"and b9["text"]=="O" and b10["text"]=="O":
        b6.config(bg="white",fg="black")
        b7.config(bg="white",fg="black")
        b8.config(bg="white",fg="black")
        b9.config(bg="white",fg="black")
        b10.config(bg="white",fg="black")
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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
    elif b11["text"]=="O" and b12["text"]=="O" and b13["text"]=="O"and b14["text"]=="O" and b15["text"]=="O":
        b11.config(bg="white",fg="black")
        b12.config(bg="white",fg="black")
        b13.config(bg="white",fg="black")
        b14.config(bg="white",fg="black")
        b15.config(bg="white",fg="black")
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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
    elif b16["text"]=="O" and b17["text"]=="O" and b18["text"]=="O"and b19["text"]=="O" and b20["text"]=="O":
        b16.config(bg="white",fg="black")
        b17.config(bg="white",fg="black")
        b18.config(bg="white",fg="black")
        b19.config(bg="white",fg="black")
        b20.config(bg="white",fg="black")
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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
    elif b21["text"]=="O" and b22["text"]=="O" and b23["text"]=="O"and b24["text"]=="O" and b25["text"]=="O":
        b21.config(bg="white",fg="black")
        b22.config(bg="white",fg="black")
        b23.config(bg="white",fg="black")
        b24.config(bg="white",fg="black")
        b25.config(bg="white",fg="black")
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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

    elif b1["text"]=="O" and b6["text"]=="O" and b11["text"]=="O" and b16["text"]=="O" and b21["text"]=="O":
        b1.config(bg="white",fg="black")
        b6.config(bg="white",fg="black")
        b11.config(bg="white",fg="black")
        b16.config(bg="white",fg="black")
        b21.config(bg="white",fg="black")
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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
	
    elif b2["text"]=="O" and b7["text"]=="O" and b12["text"]=="O" and b17["text"]=="O" and b22["text"]=="O":
        b2.config(bg="white",fg="black")
        b7.config(bg="white",fg="black")
        b12.config(bg="white",fg="black")
        b17.config(bg="white",fg="black")
        b22.config(bg="white",fg="black")
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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
      
    elif b3["text"]=="O" and b8["text"]=="O" and b13["text"]=="O" and b18["text"]=="O" and b23["text"]=="O":
        b3.config(bg="white",fg="black")
        b8.config(bg="white",fg="black")
        b13.config(bg="white",fg="black")
        b18.config(bg="white",fg="black")
        b23.config(bg="white",fg="black")
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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

    elif b4["text"]=="O" and b9["text"]=="O" and b14["text"]=="O" and b19["text"]=="O" and b24["text"]=="O":
        b4.config(bg="white",fg="black")
        b9.config(bg="white",fg="black")
        b14.config(bg="white",fg="black")
        b19.config(bg="white",fg="black")
        b24.config(bg="white",fg="black")
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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

    elif b5["text"]=="O" and b10["text"]=="O" and b15["text"]=="O" and b20["text"]=="O" and b25["text"]=="O":
        b5.config(bg="white",fg="black")
        b10.config(bg="white",fg="black")
        b15.config(bg="white",fg="black")
        b20.config(bg="white",fg="black")
        b25.config(bg="white",fg="black")
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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
    
    elif b1["text"]=="O" and b7["text"]=="O" and b13["text"]=="O" and b19["text"]=="O" and b25["text"]=="O":
        b1.config(bg="white",fg="black")
        b7.config(bg="white",fg="black")
        b13.config(bg="white",fg="black")
        b19.config(bg="white",fg="black")
        b25.config(bg="white",fg="black") 
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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
    elif b5["text"]=="O" and b9["text"]=="O" and b13["text"]=="O" and b17["text"]=="O" and b21["text"]=="O":
        b5.config(bg="white",fg="black")
        b9.config(bg="white",fg="black")
        b13.config(bg="white",fg="black")
        b17.config(bg="white",fg="black")
        b21.config(bg="white",fg="black") 
        winner=True
        scoreO=1
        a=f.readlines()
        t=open("Score.txt",'w')
        if len(a)==2:
            scoreX=scoreX+int(a[0])
            scoreO=scoreO+int(a[1])
            t.write(str(scoreX)+"\n"+str(scoreO)+"\n")
        else:
            scoreX=scoreX+int(a[len(a)-2])
            scoreO=scoreO+int(a[len(a)-1])
            for i in range(len(a)-2):
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

    if count==25 and winner==False:
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
l1=Label(root,text="LEVEL-2",font=("Algerian",26),height=2,width=7,bg="#E39FF6",fg="black")
l1.place(x=240,y=50)
l2=Label(root,text="SCORE:",font=("Algerian",22),height=2,bg="#E39FF6",fg="black")
l2.place(x=500,y=50)

l3=Label(root,text=pX.rstrip('\n')+"(X): "+str(X),font=("Times New Roman",20),height=2,bg="#E39FF6",fg="black")
l3.place(x=500,y=100)
l4=Label(root,text=pO.rstrip('\n')+"(O): "+str(O),font=("Times New Roman",20),height=2,bg="#E39FF6",fg="black")
l4.place(x=500,y=150)
#Note:Lambda is used to for anything(variable) to be passed into a function
b1=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="#ff033e",command=lambda:click(b1))
b2=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="#ff033e",command=lambda:click(b2))
b3=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="#ff033e",command=lambda:click(b3))

b4=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="#ff033e",command=lambda:click(b4))
b5=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="#ff033e",command=lambda:click(b5))
b6=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="#bf00ff",command=lambda:click(b6))

b7=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="#bf00ff",command=lambda:click(b7))
b8=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="#bf00ff",command=lambda:click(b8))
b9=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="#bf00ff",command=lambda:click(b9))
b10=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="#bf00ff",command=lambda:click(b10))

b11=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="yellow",command=lambda:click(b11))
b12=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="yellow",command=lambda:click(b12))
b13=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="yellow",command=lambda:click(b13))

b14=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="yellow",command=lambda:click(b14))
b15=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="yellow",command=lambda:click(b15))
b16=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="#b78727",command=lambda:click(b16))

b17=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="#b78727",command=lambda:click(b17))
b18=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="#b78727",command=lambda:click(b18))
b19=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="#b78727",command=lambda:click(b19))

b20=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="#b78727",command=lambda:click(b20))
b21=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="Aquamarine",command=lambda:click(b21))
b22=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="Aquamarine",command=lambda:click(b22))
b23=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="Aquamarine",command=lambda:click(b23))

b24=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="Aquamarine",command=lambda:click(b24))
b25=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="Aquamarine",command=lambda:click(b25))

b1.place(x=140,y=135)
b2.place(x=210,y=135)
b3.place(x=280,y=135)
b4.place(x=350,y=135)
b5.place(x=420,y=135)

b6.place(x=140,y=210)
b7.place(x=210,y=210)
b8.place(x=280,y=210)
b9.place(x=350,y=210)
b10.place(x=420,y=210)

b11.place(x=140,y=285)
b12.place(x=210,y=285)
b13.place(x=280,y=285)
b14.place(x=350,y=285)
b15.place(x=420,y=285)

b16.place(x=140,y=360)
b17.place(x=210,y=360)
b18.place(x=280,y=360)
b19.place(x=350,y=360)
b20.place(x=420,y=360)

b21.place(x=140,y=435)
b22.place(x=210,y=435)
b23.place(x=280,y=435)
b24.place(x=350,y=435)
b25.place(x=420,y=435)

root.mainloop()