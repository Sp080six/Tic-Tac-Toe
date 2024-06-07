from tkinter import *
from tkinter import scrolledtext

root=Tk()
root.title("Score_Board")
root.geometry('500x600')
root.configure(background="yellow")
    
l1=Label(root,text="SCORE_BOARD",font=("Algerian",26),height=2,bg="yellow",fg="black")
l1.place(x=135,y=10)
f=open("Score.txt")
t=open("Name.txt")
a=f.readlines()    
b=t.readlines()
f.close()
t.close()
frame=Frame(root)
scrollbar=Scrollbar(frame)
text_area = scrolledtext.ScrolledText(frame,wrap=WORD,width=25,height=10,font = ("Times New Roman",14))
frame.grid(row=0,column=0,padx=120,pady=100)

text_area.grid(row=0)
text_area.insert(INSERT,"Name"+'\t\t'+"Score"+'\n'+'*************************'+'\n')
rows=1
for i in range(len(a)):
        c=b[i].rstrip('\n')
        if i%2==0:
           text_area.grid(row=rows,pady=10, padx=10)
           text_area.insert(INSERT,c+'\t\t'+str(a[i]))
        else:
            text_area.grid(row=rows,pady=10, padx=10)
            text_area.insert(INSERT,c+'\t\t'+str(a[i])+'*************************'+'\n')
        rows=rows+1
photo = PhotoImage(file =r"C:\Users\veda2\OneDrive\Documents\Tic_Tac_Toe\Congratulations.png")
photoimage = photo.subsample(1,1)
Button(root, image = photoimage).place(x=90,y=350)         
root.mainloop()