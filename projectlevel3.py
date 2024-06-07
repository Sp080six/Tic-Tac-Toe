from tkinter import *
from tkinter import messagebox
import os

root=Tk()
root.geometry("900x1000")
root.title("Tic-Tac-Toe")
root.configure(bg="black")

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
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)
    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)
    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)
    b37.config(state=DISABLED)
    b38.config(state=DISABLED)
    b39.config(state=DISABLED)
    b40.config(state=DISABLED)
    b41.config(state=DISABLED)
    b42.config(state=DISABLED)
    b43.config(state=DISABLED)
    b44.config(state=DISABLED)
    b45.config(state=DISABLED)
    b46.config(state=DISABLED)
    b47.config(state=DISABLED)
    b48.config(state=DISABLED)
    b49.config(state=DISABLED)
    l3.destroy()
    l4.destroy()
    l5=Label(root,text=pX.rstrip('\n')+"(X): "+str(X),font=("Times New Roman",20),bg="black",fg="white")
    l5.place(x=650,y=100)
    l6=Label(root,text=pO.rstrip('\n')+"(O): "+str(O),font=("Times New Roman",20),bg="black",fg="white")
    l6.place(x=650,y=150)
#To see if anyone won
def won():
    global scoreX
    global scoreO
    global f
    global X
    global O
    global winner
    winner=False
    #X Won
    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X" and b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X" and b7["text"]=="X":
        b1.config(bg="yellow",fg="black")
        b2.config(bg="yellow",fg="black")
        b3.config(bg="yellow",fg="black")
        b4.config(bg="yellow",fg="black")
        b5.config(bg="yellow",fg="black")
        b6.config(bg="yellow",fg="black")
        b7.config(bg="yellow",fg="black")
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
    elif b8["text"]=="X" and b9["text"]=="X" and b10["text"]=="X" and b11["text"]=="X" and b12["text"]=="X" and b13["text"]=="X" and b14["text"]=="X":
        b8.config(bg="yellow",fg="black")
        b9.config(bg="yellow",fg="black")
        b10.config(bg="yellow",fg="black")
        b11.config(bg="yellow",fg="black")
        b12.config(bg="yellow",fg="black")
        b13.config(bg="yellow",fg="black")
        b14.config(bg="yellow",fg="black")
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
    elif b15["text"]=="X" and b16["text"]=="X" and b17["text"]=="X" and b18["text"]=="X" and b19["text"]=="X" and b20["text"]=="X" and b21["text"]=="X":
        b15.config(bg="")
        b16.config(bg="yellow",fg="black")
        b17.config(bg="yellow",fg="black")
        b18.config(bg="yellow",fg="black")
        b19.config(bg="yellow",fg="black")
        b20.config(bg="yellow",fg="black")
        b21.config(bg="yellow",fg="black")
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
    elif b22["text"]=="X" and b23["text"]=="X" and b24["text"]=="X" and b25["text"]=="X" and b26["text"]=="X" and b27["text"]=="X" and b28["text"]=="X":    
        b22.config(bg="yellow",fg="black")
        b23.config(bg="yellow",fg="black")
        b24.config(bg="yellow",fg="black")
        b25.config(bg="yellow",fg="black")
        b26.config(bg="yellow",fg="black")
        b27.config(bg="yellow",fg="black")
        b28.config(bg="yellow",fg="black")
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
    elif b29["text"]=="X" and b30["text"]=="X" and b31["text"]=="X" and b32["text"]=="X" and b33["text"]=="X" and b34["text"]=="X" and b35["text"]=="X":    
        b29.config(bg="yellow",fg="black")
        b30.config(bg="yellow",fg="black")
        b31.config(bg="yellow",fg="black")
        b32.config(bg="yellow",fg="black")
        b33.config(bg="yellow",fg="black")
        b34.config(bg="yellow",fg="black")
        b35.config(bg="yellow",fg="black")
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
    elif b36["text"]=="X" and b37["text"]=="X" and b38["text"]=="X" and b39["text"]=="X" and b40["text"]=="X" and b41["text"]=="X" and b42["text"]=="X":    
        b36.config(bg="yellow",fg="black")
        b37.config(bg="yellow",fg="black")
        b38.config(bg="yellow",fg="black")
        b39.config(bg="yellow",fg="black")
        b40.config(bg="yellow",fg="black")
        b41.config(bg="yellow",fg="black")
        b42.config(bg="yellow",fg="black")
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
    elif b43["text"]=="X" and b44["text"]=="X" and b45["text"]=="X" and b46["text"]=="X" and b47["text"]=="X" and b48["text"]=="X" and b49["text"]=="X":    
        b43.config(bg="yellow",fg="black")
        b44.config(bg="yellow",fg="black")
        b45.config(bg="yellow",fg="black")
        b46.config(bg="yellow",fg="black")
        b47.config(bg="yellow",fg="black")
        b48.config(bg="yellow",fg="black")
        b49.config(bg="yellow",fg="black")
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
    elif b1["text"]=="X" and b8["text"]=="X" and b15["text"]=="X" and b22["text"]=="X" and b29["text"]=="X" and b36["text"]=="X" and b43["text"]=="X":    
        b1.config(bg="yellow",fg="black")
        b8.config(bg="yellow",fg="black")
        b15.config(bg="yellow",fg="black")
        b22.config(bg="yellow",fg="black")
        b29.config(bg="yellow",fg="black")
        b36.config(bg="yellow",fg="black")
        b43.config(bg="yellow",fg="black")
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
    elif b2["text"]=="X" and b9["text"]=="X" and b16["text"]=="X" and b23["text"]=="X" and b30["text"]=="X" and b37["text"]=="X" and b44["text"]=="X":    
        b2.config(bg="yellow",fg="black")
        b9.config(bg="yellow",fg="black")
        b16.config(bg="yellow",fg="black")
        b23.config(bg="yellow",fg="black")
        b30.config(bg="yellow",fg="black")
        b37.config(bg="yellow",fg="black")
        b44.config(bg="yellow",fg="black")
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
    elif b3["text"]=="X" and b10["text"]=="X" and b17["text"]=="X" and b24["text"]=="X" and b31["text"]=="X" and b38["text"]=="X" and b45["text"]=="X":    
        b3.config(bg="yellow",fg="black")
        b10.config(bg="yellow",fg="black")
        b17.config(bg="yellow",fg="black")
        b24.config(bg="yellow",fg="black")
        b31.config(bg="yellow",fg="black")
        b38.config(bg="yellow",fg="black")
        b45.config(bg="yellow",fg="black")
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
    elif b4["text"]=="X" and b11["text"]=="X" and b18["text"]=="X" and b25["text"]=="X" and b32["text"]=="X" and b39["text"]=="X" and b46["text"]=="X":    
        b4.config(bg="yellow",fg="black")
        b11.config(bg="yellow",fg="black")
        b18.config(bg="yellow",fg="black")
        b25.config(bg="yellow",fg="black")
        b32.config(bg="yellow",fg="black")
        b39.config(bg="yellow",fg="black")
        b46.config(bg="yellow",fg="black")
        winner=True
        messagebox.showinfo("Tic-Tac-Toe","Congratulations X wins")
        disable()                         
    elif b5["text"]=="X" and b12["text"]=="X" and b19["text"]=="X" and b26["text"]=="X" and b33["text"]=="X" and b40["text"]=="X" and b47["text"]=="X":    
        b5.config(bg="yellow",fg="black")
        b12.config(bg="yellow",fg="black")
        b19.config(bg="yellow",fg="black")
        b26.config(bg="yellow",fg="black")
        b33.config(bg="yellow",fg="black")
        b40.config(bg="yellow",fg="black")
        b47.config(bg="yellow",fg="black")
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
    elif b6["text"]=="X" and b13["text"]=="X" and b20["text"]=="X" and b27["text"]=="X" and b34["text"]=="X" and b41["text"]=="X" and b48["text"]=="X":    
        b6.config(bg="yellow",fg="black")
        b13.config(bg="yellow",fg="black")
        b20.config(bg="yellow",fg="black")
        b27.config(bg="yellow",fg="black")
        b34.config(bg="yellow",fg="black")
        b41.config(bg="yellow",fg="black")
        b48.config(bg="yellow",fg="black")
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
    elif b7["text"]=="X" and b14["text"]=="X" and b21["text"]=="X" and b28["text"]=="X" and b35["text"]=="X" and b42["text"]=="X" and b49["text"]=="X":    
        b7.config(bg="yellow",fg="black")
        b14.config(bg="yellow",fg="black")
        b21.config(bg="yellow",fg="black")
        b28.config(bg="yellow",fg="black")
        b35.config(bg="yellow",fg="black")
        b42.config(bg="yellow",fg="black")
        b49.config(bg="yellow",fg="black")
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
    elif b1["text"]=="X" and b9["text"]=="X" and b17["text"]=="X" and b25["text"]=="X" and b33["text"]=="X" and b41["text"]=="X" and b49["text"]=="X":    
        b1.config(bg="yellow",fg="black")
        b9.config(bg="yellow",fg="black")
        b17.config(bg="yellow",fg="black")
        b25.config(bg="yellow",fg="black")
        b33.config(bg="yellow",fg="black")
        b41.config(bg="yellow",fg="black")
        b49.config(bg="yellow",fg="black")
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
    elif b7["text"]=="X" and b13["text"]=="X" and b19["text"]=="X" and b25["text"]=="X" and b31["text"]=="X" and b37["text"]=="X" and b43["text"]=="X":    
        b7.config(bg="yellow",fg="black")
        b13.config(bg="yellow",fg="black")
        b19.config(bg="yellow",fg="black")
        b25.config(bg="yellow",fg="black")
        b31.config(bg="yellow",fg="black")
        b37.config(bg="yellow",fg="black")
        b43.config(bg="yellow",fg="black")
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
    elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O" and b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O" and b7["text"]=="O":
        b1.config(bg="yellow",fg="black")
        b2.config(bg="yellow",fg="black")
        b3.config(bg="yellow",fg="black")
        b4.config(bg="yellow",fg="black")
        b5.config(bg="yellow",fg="black")
        b6.config(bg="yellow",fg="black")
        b7.config(bg="yellow",fg="black")
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
    elif b8["text"]=="O" and b9["text"]=="O" and b10["text"]=="O" and b11["text"]=="O" and b12["text"]=="O" and b13["text"]=="O" and b14["text"]=="O":
        b8.config(bg="yellow",fg="black")
        b9.config(bg="yellow",fg="black")
        b10.config(bg="yellow",fg="black")
        b11.config(bg="yellow",fg="yellow")
        b12.config(bg="yellow",fg="black")
        b13.config(bg="yellow",fg="black")
        b14.config(bg="yellow",fg="black")
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
    elif b15["text"]=="O" and b16["text"]=="O" and b17["text"]=="O" and b18["text"]=="O" and b19["text"]=="O" and b20["text"]=="O" and b21["text"]=="O":
        b15.config(bg="yellow",fg="black")
        b16.config(bg="yellow",fg="black")
        b17.config(bg="yellow",fg="black")
        b18.config(bg="yellow",fg="black")
        b19.config(bg="yellow",fg="black")
        b20.config(bg="yellow",fg="black")
        b21.config(bg="yellow",fg="black")
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
    elif b22["text"]=="O" and b23["text"]=="O" and b24["text"]=="O" and b25["text"]=="O" and b26["text"]=="O" and b27["text"]=="O" and b28["text"]=="O":    
        b22.config(bg="yellow",fg="black")
        b23.config(bg="yellow",fg="black")
        b24.config(bg="yellow",fg="black")
        b25.config(bg="yellow",fg="black")
        b26.config(bg="yellow",fg="black")
        b27.config(bg="yellow",fg="black")
        b28.config(bg="yellow",fg="black")
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
    elif b29["text"]=="O" and b30["text"]=="O" and b31["text"]=="O" and b32["text"]=="O" and b33["text"]=="O" and b34["text"]=="O" and b35["text"]=="O":    
        b29.config(bg="yellow",fg="black")
        b30.config(bg="yellow",fg="black")
        b31.config(bg="yellow",fg="black")
        b32.config(bg="yellow",fg="black")
        b33.config(bg="yellow",fg="black")
        b34.config(bg="yellow",fg="black")
        b35.config(bg="yellow",fg="black")
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
    elif b36["text"]=="O" and b37["text"]=="O" and b38["text"]=="O" and b39["text"]=="O" and b40["text"]=="O" and b41["text"]=="O" and b42["text"]=="O":    
        b36.config(bg="yellow",fg="black")
        b37.config(bg="yellow",fg="black")
        b38.config(bg="yellow",fg="black")
        b39.config(bg="yellow",fg="black")
        b40.config(bg="yellow",fg="black")
        b41.config(bg="yellow",fg="black")
        b42.config(bg="yellow",fg="black")
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
    elif b43["text"]=="O" and b44["text"]=="O" and b45["text"]=="O" and b46["text"]=="O" and b47["text"]=="O" and b48["text"]=="O" and b49["text"]=="O":    
        b43.config(bg="yellow",fg="black")
        b44.config(bg="yellow",fg="black")
        b45.config(bg="yellow",fg="black")
        b46.config(bg="yellow",fg="black")
        b47.config(bg="yellow",fg="black")
        b48.config(bg="yellow",fg="black")
        b49.config(bg="yellow",fg="black")
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
    elif b1["text"]=="O" and b8["text"]=="O" and b15["text"]=="O" and b22["text"]=="O" and b29["text"]=="O" and b36["text"]=="O" and b43["text"]=="O":    
        b1.config(bg="yellow",fg="black")
        b8.config(bg="yellow",fg="black")
        b15.config(bg="yellow",fg="black")
        b22.config(bg="yellow",fg="black")
        b29.config(bg="yellow",fg="black")
        b36.config(bg="yellow",fg="black")
        b43.config(bg="yellow",fg="black")
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
    elif b2["text"]=="O" and b9["text"]=="O" and b16["text"]=="O" and b23["text"]=="O" and b30["text"]=="O" and b37["text"]=="O" and b44["text"]=="O":    
        b2.config(bg="yellow",fg="black")
        b9.config(bg="yellow",fg="black")
        b16.config(bg="yellow",fg="black")
        b23.config(bg="yellow",fg="black")
        b30.config(bg="yellow",fg="black")
        b37.config(bg="yellow",fg="black")
        b44.config(bg="yellow",fg="black")
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
    elif b3["text"]=="O" and b10["text"]=="O" and b17["text"]=="O" and b24["text"]=="O" and b31["text"]=="O" and b38["text"]=="O" and b45["text"]=="O":    
        b3.config(bg="yellow",fg="black")
        b10.config(bg="yellow",fg="black")
        b17.config(bg="yellow",fg="black")
        b24.config(bg="yellow",fg="black")
        b31.config(bg="yellow",fg="black")
        b38.config(bg="yellow",fg="black")
        b45.config(bg="yellow",fg="black")
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
    elif b4["text"]=="O" and b11["text"]=="O" and b18["text"]=="O" and b25["text"]=="O" and b32["text"]=="O" and b39["text"]=="O" and b46["text"]=="O":    
        b4.config(bg="yellow",fg="black")
        b11.config(bg="yellow",fg="black")
        b18.config(bg="yellow",fg="black")
        b25.config(bg="yellow",fg="black")
        b32.config(bg="yellow",fg="black")
        b39.config(bg="yellow",fg="black")
        b46.config(bg="yellow",fg="black")
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
    elif b5["text"]=="O" and b12["text"]=="O" and b19["text"]=="O" and b26["text"]=="O" and b33["text"]=="O" and b40["text"]=="O" and b47["text"]=="O":    
        b5.config(bg="yellow",fg="black")
        b12.config(bg="yellow",fg="black")
        b19.config(bg="yellow",fg="black")
        b26.config(bg="yellow",fg="black")
        b33.config(bg="yellow",fg="black")
        b40.config(bg="yellow",fg="black")
        b47.config(bg="yellow",fg="black")
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
    elif b6["text"]=="O" and b13["text"]=="O" and b20["text"]=="O" and b27["text"]=="O" and b34["text"]=="O" and b41["text"]=="O" and b48["text"]=="O":    
        b6.config(bg="yellow",fg="black")
        b13.config(bg="yellow",fg="black")
        b20.config(bg="yellow",fg="black")
        b27.config(bg="yellow",fg="black")
        b34.config(bg="yellow",fg="black")
        b41.config(bg="yellow",fg="black")
        b48.config(bg="yellow",fg="black")
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
    elif b7["text"]=="O" and b14["text"]=="O" and b21["text"]=="O" and b28["text"]=="O" and b35["text"]=="O" and b42["text"]=="O" and b49["text"]=="O":    
        b7.config(bg="yellow",fg="black")
        b14.config(bg="yellow",fg="black")
        b21.config(bg="yellow",fg="black")
        b28.config(bg="yellow",fg="black")
        b35.config(bg="yellow",fg="black")
        b42.config(bg="yellow",fg="black")
        b49.config(bg="yellow",fg="black")
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
    elif b1["text"]=="O" and b9["text"]=="O" and b17["text"]=="O" and b25["text"]=="O" and b33["text"]=="O" and b41["text"]=="O" and b49["text"]=="O":    
        b1.config(bg="yellow",fg="black")
        b9.config(bg="yellow",fg="black")
        b17.config(bg="yellow",fg="black")
        b25.config(bg="yellow",fg="black")
        b33.config(bg="yellow",fg="black")
        b41.config(bg="yellow",fg="black")
        b49.config(bg="yellow",fg="black")
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
    elif b7["text"]=="O" and b13["text"]=="O" and b19["text"]=="O" and b25["text"]=="O" and b31["text"]=="O" and b37["text"]=="O" and b43["text"]=="O":    
        b7.config(bg="yellow",fg="black")
        b13.config(bg="yellow",fg="black")
        b19.config(bg="yellow",fg="black")
        b25.config(bg="yellow",fg="black")
        b31.config(bg="yellow",fg="black")
        b37.config(bg="yellow",fg="black")
        b43.config(bg="yellow",fg="black")
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
    if count==49 and winner==False:
        a=f.readlines()
        for i in range(len(a)):
            X=a[len(a)-2]
            O=a[len(a)-1]
        f.close()
        messagebox.showinfo("Tic-Tac-Toe","It's a tie..Hence no one wins!")
        disable()
    if winner==True or count==49:
      if X>O:
        messagebox.showinfo("Tic-Tac-Toe","CONGRATULATIONS!!!!\n"+pX.rstrip('\n').upper()+" WINS THE GAME")
        root.destroy()
        os.system("Score_Board.py")
      elif O>X:
        messagebox.showinfo("Tic-Tac-Toe","CONGRATULATIONS!!!!\n"+pO.rstrip('\n').upper()+" WINS THE GAME")
        root.destroy()
        os.system("Score_Board.py")
      else:
        messagebox.showinfo("Tic-Tac-Toe","THE GAME IS A TIE")
        root.destroy()
        os.system("Score_Board.py")
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
#Note:Lambda is used to for anything(variable) to be passed into a function
l1=Label(root,text="LEVEL-3",font=("Algerian",26),height=2,width=8,bg="black",fg="white")
l1.place(x=330,y=50)
l2=Label(root,text="SCORE:",font=("Algerian",22),height=2,bg="black",fg="white")
l2.place(x=650,y=50)
l3=Label(root,text=pX.rstrip('\n')+"(X): "+str(X),font=("Times New Roman",20),bg="black",fg="white")
l3.place(x=650,y=100)
l4=Label(root,text=pO.rstrip('\n')+"(O): "+str(O),font=("Times New Roman",20),bg="black",fg="white")
l4.place(x=650,y=150)
b1=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b1))
b2=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b2))
b3=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b3))

b4=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b4))
b5=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b5))
b6=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b6))

b7=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b7))
b8=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b8))
b9=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b9))

b10=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b10))
b11=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b11))
b12=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b12))

b13=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b13))
b14=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b14))
b15=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b15))

b16=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b16))
b17=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b17))
b18=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b18))

b19=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b19))
b20=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b20))
b21=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b21))

b22=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b22))
b23=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b23))
b24=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b24))

b25=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b25))
b26=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b26))
b27=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b27))

b28=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b28))
b29=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b29))
b30=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b30))

b31=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b31))
b32=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b32))
b33=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b33))

b34=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b34))
b35=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b35))
b36=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b36))

b37=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b37))
b38=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b38))
b39=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b39))

b40=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b40))
b41=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b41))
b42=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b42))

b43=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b43))
b44=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b44))
b45=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b45))

b46=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b46))
b47=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b47))
b48=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="white",fg="black",command=lambda:click(b48))

b49=Button(root,text=" ",font=("Times New Roman",20),height=2,width=4,bg="black",fg="white",command=lambda:click(b49))

b1.place(x=140,y=135)
b2.place(x=210,y=135)
b3.place(x=280,y=135)
b4.place(x=350,y=135)
b5.place(x=420,y=135)
b6.place(x=490,y=135)
b7.place(x=560,y=135)

b8.place(x=140,y=210)
b9.place(x=210,y=210)
b10.place(x=280,y=210)
b11.place(x=350,y=210)
b12.place(x=420,y=210)
b13.place(x=490,y=210)
b14.place(x=560,y=210)

b15.place(x=140,y=285)
b16.place(x=210,y=285)
b17.place(x=280,y=285)
b18.place(x=350,y=285)
b19.place(x=420,y=285)
b20.place(x=490,y=285)
b21.place(x=560,y=285)

b22.place(x=140,y=360)
b23.place(x=210,y=360)
b24.place(x=280,y=360)
b25.place(x=350,y=360)
b26.place(x=420,y=360)
b27.place(x=490,y=360)
b28.place(x=560,y=360)

b29.place(x=140,y=435)
b30.place(x=210,y=435)
b31.place(x=280,y=435)
b32.place(x=350,y=435)
b33.place(x=420,y=435)
b34.place(x=490,y=435)
b35.place(x=560,y=435)

b36.place(x=140,y=510)
b37.place(x=210,y=510)
b38.place(x=280,y=510)
b39.place(x=350,y=510)
b40.place(x=420,y=510)
b41.place(x=490,y=510)
b42.place(x=560,y=510)

b43.place(x=140,y=585)
b44.place(x=210,y=585)
b45.place(x=280,y=585)
b46.place(x=350,y=585)
b47.place(x=420,y=585)
b48.place(x=490,y=585)
b49.place(x=560,y=585)

root.mainloop()
