'''from tkinter import *
import os
w=Tk()
w.title("HOW TO PLAY")
w.geometry("1200x450")
w.configure(bg="black")
def call_newscreen():
    w.destroy()
    os.system("Rules.py")
l7=Label(w,text="H O W  T O  P L A Y :",font=("Times New Roman",18),bg="black",fg="white")
l1=Label(w,text="* X always goes first in tic tac toe, after that player take turns in placing Xs and Os on the playing board until the game is over",font=("Times New Roman",14),height=2,bg="black",fg="#ffc655")
l2=Label(w,text="* The game is over when either one of the players has all the X's or O's in a row/column/diagonal",font=("Times New Roman",14),height=2,bg="black",fg="#00faf7")
l3=Label(w,text="* The player who first gets all the X's or O's in row/column/diagoal wins the game.If the playing board is full and there is still no winner, it will result in a draw",font=("Times New Roman",14),height=2,bg="black",fg="#ffc655")
l4=Label(w,text="* Note that in case there are more than 1 coloum/row/diagonal with all X's or all O's only 1 among that will be considered",font=("Times New Roman",14),height=2,bg="black",fg="#00faf7")                
l5=Label(w,text="* You can play tic tac toe against your  family and friends",font=("Times New Roman",14),height=2,bg="black",fg="#ffc655")         
l6=Label(w,text="* This game will consists of three levels",font=("Times New Roman",14),height=2,bg="black",fg="#00faf7")

l1.place(x=0,y=50)
l2.place(x=0,y=100)
l3.place(x=0,y=150)
l4.place(x=0,y=200)
l5.place(x=0,y=250)
l6.place(x=0,y=300)
l7.place(x=0,y=0)
btn_next=Button(w,text="NEXT",command=call_newscreen,bg="black",fg="white",font=("Times New Roman",18))
btn_next.place(x=20,y=350)
w.mainloop()'''
class point:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def __add__(self,obj):
		return(self.a+obj.a,self.b+obj.b)
p1=point(1,2)
p2=point(2,3)
p3=p1+p2
print(p3)